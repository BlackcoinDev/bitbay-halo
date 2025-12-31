import os
import re
import sys
import ast
import traceback
import logging
import password
import base64
import smtplib
import imaplib
import pyzmail
import time
import stopit
import email
import quopri

from BitMHalo_shared import shared

app_dir = os.path.dirname(os.path.abspath(__file__))+'/./src'
sys.path.insert(0, app_dir)

from highlevelcrypto import decrypt


providers = [{'@gmail': {'imap': 'imap.googlemail.com', 'smtp': 'smtp.googlemail.com', 'port': 587, 'SSL': 0}},
             {'@hotmail': {'imap': 'imap-mail.outlook.com',
                           'smtp': 'smtp-mail.outlook.com', 'port': 587, 'SSL': 0}},
             {'@outlook': {'imap': 'imap-mail.outlook.com',
                           'smtp': 'smtp-mail.outlook.com', 'port': 587, 'SSL': 0}},
             {'@aol.com': {'imap': 'imap.aol.com', 'smtp': 'smtp.aol.com', 'port': 587, 'SSL': 0}}]

content_chk1 = "You have received a payment of "
content_chk2 = "If you are new to Cryptocurrency, somebody may have sent you these coins"

logger = logging.getLogger('console')


def is_email_provider_supported(from_addr):
    verified = False
    imap_name = None
    smtp_name = None
    port = None
    is_ssl = None
    for provider in providers:
        for at_addr, val in provider.items():
            if at_addr in from_addr.lower():
                verified = True
                imap_name = provider[at_addr]['imap']
                smtp_name = provider[at_addr]['smtp']
                port = provider[at_addr]['port']
                is_ssl = provider[at_addr]['SSL']
                break
    return verified, imap_name, smtp_name, port, is_ssl


def test_is_email_provider_supported():
    assert is_email_provider_supported("xxx@gmail.com")[0]
    assert is_email_provider_supported("xxx@hotmail.com")[0]
    assert is_email_provider_supported("xxx@outlook.com")[0]
    assert is_email_provider_supported("xxx@aol.com")[0]
    assert not is_email_provider_supported("xxx@unknown.com")[0]


def is_email(data):
    from_address = ""
    if "ENCRYPTED:" in data:
        if "PASSWORD:" in data:
            match_obj = re.match(r'(PASSWORD:)(.*?)(MY:)', data, re.M | re.I)
            email_password = match_obj.group(2)
            data = data.replace("PASSWORD:" + email_password, "")
        match_obj = re.match(
            r'(MY:)(.*?)(THEIR:)(.*?)(ENCRYPTED:)(.*?)(###)', data, re.M | re.I)
        from_address = match_obj.group(2)
        to_address = match_obj.group(4)
    else:
        try:
            content = ast.literal_eval(data)
            from_address = content['MyBMAddress']
            to_address = content['TheirBMAddress']
        except Exception, e:
            logger.error("bitmhalo: outbox parsing: %s %s" %
                         (str(e), traceback.format_exc()))
            to_address = "####"

    if "@" in to_address:
        return True, from_address

    return False, from_address


def exctract_email_data(data):
    email_password = ""
    from_address = ""
    content = ""
    if "ENCRYPTED:" in data:
        if "PASSWORD:" in data:
            match_obj = re.match(r'(PASSWORD:)(.*?)(MY:)', data, re.M | re.I)
            email_password = match_obj.group(2)
            data = data.replace("PASSWORD:" + email_password, "")
        match_obj = re.match(
            r'(MY:)(.*?)(THEIR:)(.*?)(ENCRYPTED:)(.*?)(###)', data, re.M | re.I)
        content = match_obj.group(5) + match_obj.group(6)
        from_address = match_obj.group(2)
        to_address = match_obj.group(4)
    else:
        try:
            content = ast.literal_eval(data)
            from_address = content['MyBMAddress']
            to_address = content['TheirBMAddress']
            if 'password' in content:
                email_password = content['password']
                content.pop("password", None)
        except Exception, e:
            logger.error("bitmhalo: outbox parsing: %s %s" %
                         (str(e), traceback.format_exc()))
            to_address = "####"

    return from_address, to_address, content, email_password


def send_email(email_password, content, from_address, to_address, smtp_name, port):
    try:
        email_password = password.DecryptWithAES("Halo Master", email_password)
    except Exception, e:
        logger.error("bitmhalo: password decryption: %s %s" %
                     (str(e), traceback.format_exc()))

    if content_chk1 not in str(content) and content_chk2 not in str(content):
        return send_email_smtp(email_password, content, from_address, to_address, smtp_name, port)
    else:
        return send_email_pyzmail(email_password, content, from_address, to_address, smtp_name, port)


def send_email_smtp(email_password, content, from_address, to_address, smtp_name, port):
    try:
        connection = smtplib.SMTP(smtp_name, port)
        connection.ehlo()
        connection.starttls()
        content="****"+str(content)+"****"
        headers = ["from: " + from_address, "subject: " + "Halo", "to: " + to_address, "mime-version: 1.0",
                   "content-type: text/html"]
        headers = "\r\n".join(headers)
        connection.login(from_address, email_password)
        connection.sendmail(from_address, to_address,
                            headers + "\r\n\r\n" + str(content))
        connection.close()
    except Exception, e:
        logger.error("bitmhalo: smtp send: %s, %s" %
                     (str(e), traceback.format_exc()))
        return False

    return True


def send_email_pyzmail(email_password, content, from_address, to_address, smtp_name, port):
    try:
        b64 = base64.b64decode(content['b64img'])
        text_content = unicode(content['Data'])
        html_content = u'<html><body>' + content['Data'] + \
                       '<img src="cid:doge" />.\n' \
                       '</body></html>'
        payload, mail_from, rcpt_to, msg_id = pyzmail.compose_mail(
            (unicode(from_address), from_address),
            [(unicode(to_address), to_address)],
            u'Halo',
            'iso-8859-1',
            (text_content, 'iso-8859-1'),
            (html_content, 'iso-8859-1'),
            embeddeds=[(b64, 'image', 'bmp', 'doge', None), ])

        ret = pyzmail.send_mail(payload, from_address, to_address, smtp_name, smtp_port=port,
                                smtp_mode='tls', smtp_login=from_address, smtp_password=email_password)
        if isinstance(ret, dict):
            if ret:
                float("A")
            else:
                pass
        else:
            float("A")
    except Exception, e:
        logger.error("bitmhalo: smtp send: %s, %s" %
                     (str(e), traceback.format_exc()))
        return False

    return True


def resend_pending_in_outbox(outpath):
    try:
        with open(outpath, 'r') as f:
            outbox = f.readline()
            f.close()

        # Sends a message
        pos = 0
        try:
            outbox = ast.literal_eval(outbox)
        except Exception, e:
            logger.error("bitmhalo: outbox: %s %s" %
                         (str(e), traceback.format_exc()))
            outbox = []

        for data1 in outbox:  # Lets try sending some of these messages again
            time.sleep(.1)
            to_next = 1

            to_address = "####"

            is_email_data, from_address = is_email(data1)
            verified, imap_name, smtp_name, port, is_ssl = is_email_provider_supported(
                from_address)
            ret = True
            if is_email_data and verified:
                from_address, to_address, content, email_password = exctract_email_data(
                    data1)
                ret = send_email(email_password, content,
                                 from_address, to_address, smtp_name, port)
            if not ret or to_address == "####":  # We are not resending bitmessage at the moment
                outbox.pop(pos)
                to_next = 0
                with open(outpath, 'w') as f:
                    f.write(str(outbox))
                    f.flush()
                    os.fsync(f.fileno())
                    f.close()
            if to_next == 1:
                pos += 1
    except Exception, e:
        logger.error("bitmhalo: outbox: %s %s" %
                     (str(e), traceback.format_exc()))


list_response_pattern = re.compile(
    r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')


def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    mailbox_name = mailbox_name.strip('"')
    return flags, delimiter, mailbox_name


def read_inbox_messages(dat, readmessages, mailpath, imap_name, myrpc):
    ret = True
    mailbox = {}
    try:
        connection = imaplib.IMAP4_SSL(imap_name)
        connection.login(dat['Email Address'], dat['Password'])
        typ, mailbox_data = connection.list()
        inbox = []
        try:
            with open(mailpath, 'r') as f:
                mailbox = f.readline()
                f.close()
            mailbox = ast.literal_eval(mailbox)
            if mailbox == "":
                float('a')
            if dat['Email Address'] not in mailbox:
                mailbox[dat['Email Address']] = {}
        except:
            mailbox = {str(dat['Email Address']): {}}

        for line in mailbox_data:
            try:
                flags, delimiter, mailbox_name = parse_list_response(line)
                if "sent" in mailbox_name.lower() or "all" in mailbox_name.lower() or "deleted" in mailbox_name.lower() or "trash" in mailbox_name.lower() or "drafts" in mailbox_name.lower():
                    continue

                connection.select(mailbox_name, readonly=True)
                try:
                    typ, msg_ids1 = connection.uid('search', None,
                                                   '(SUBJECT "Halo")')
                    # connection.search(None, '(SUBJECT "Halo")')
                except Exception, e:
                    logger.error("bitmhalo: search: %s, %s" %
                                 (str(e), traceback.format_exc()))
                    continue

                msg_ids = msg_ids1[0]
                try:
                    msg_ids = msg_ids.split()
                except:
                    logger.error("bitmhalo: split: %s" %
                                 traceback.format_exc())

                src = ""
                src1 = ""
                mydict2 = {}
                if 'uids' in dat:
                    for elem in dat['uids']:
                        try:
                            ordnum = elem.split("#")[1]
                            orduid = elem.split("#")[0]
                            mydict2[orduid] = ordnum
                        except:
                            mydict2[elem] = ''
                for msg_id in msg_ids:
                    if 'uids' in dat:  # If they ask to skip any messages we do so
                        if msg_id in mydict2:
                            if 'ordernumber' in dat:
                                if dat['ordernumber'] == mydict2[msg_id]:
                                    pass
                                else:
                                    continue
                            else:
                                continue
                    logger.info("bitmhalo: msg_id: " + str(msg_id))
                    mymessage = {}
                    if msg_id in mailbox[str(dat['Email Address'])]:
                        try:
                            mymessage['toAddress'] = mailbox[str(
                                dat['Email Address'])][msg_id]['toAddress']
                            mymessage['fromAddress'] = mailbox[str(
                                dat['Email Address'])][msg_id]['fromAddress']
                            mymessage['body'] = mailbox[str(
                                dat['Email Address'])][msg_id]['body']
                            mymessage['uid'] = mailbox[str(
                                dat['Email Address'])][msg_id]['uid']
                            body = mymessage['body']
                        except:
                            body = ""
                            mymessage = {}
                            logger.error("bitmhalo: message read: %s" %
                                         traceback.format_exc())
                    else:
                        try:
                            if shared.systemexit == 1:  # Attempt a clean exit when possible
                                shared.systemexit = 2
                                logger.warning("bitmhalo: closing.")
                                sys.exit()
                            logger.debug("bitmhalo: fetching.")
                            # This is to prevent dropped connections, for now only on fetching
                            shared.timeresult = False
                            try:
                                # Let Halo know through RPC we started to download
                                myrpc.MessageStatus("1", "password")
                            except Exception, e:
                                pass

                            @stopit.threading_timeoutable(timeout_param='my_timeout')
                            def timethis():  # If we get dropped, we can time out
                                global typ, msg_data, connection
                                typ, msg_data = connection.uid('fetch', msg_id,
                                                               '(RFC822)')  # connection.fetch(msg_id, '(RFC822)')
                                shared.timeresult = True

                            # 10 minutes is very generous
                            timethis(my_timeout=600)
                            if shared.timeresult == False:
                                float("A")
                            try:
                                # Let Halo know through RPC we finished
                                myrpc.MessageStatus("0", "password")
                            except Exception, e:
                                pass
                            logger.debug("bitmhalo: fetched")
                        except:
                            connection.close()
                            logger.error("bitmhalo: fetch: %s" %
                                         traceback.format_exc())
                            if shared.systemexit == 2:
                                sys.exit()
                            continue
                        body = ""
                        try:
                            for part in msg_data:
                                if isinstance(part, tuple):
                                    msg = email.message_from_string(part[1])
                                    try:
                                        src = (msg['from'].split('<')[
                                               1].split('>')[0]).strip()
                                    except:
                                        src = msg['from'].strip()
                                    try:
                                        src1 = (msg['to'].split('<')[
                                                1].split('>')[0]).strip()
                                    except:
                                        src1 = msg['to'].strip()
                                    try:
                                        charset='utf8'
                                        if msg.is_multipart():
                                            for msub in msg.get_payload():
                                                if msub.get_content_charset() != None:
                                                    charset = msub.get_content_charset()
                                                body = msub.get_payload(decode = True).decode(msub.get_content_charset())
                                                break
                                        else:                                    
                                            if msg.get_content_charset() != None:
                                                charset = msg.get_content_charset()
                                            body = msg.get_payload(decode = True).decode(charset)
                                    except:
                                        try:
                                            body = str(msg.encode('utf8'))
                                        except:
                                            body = str(msg)
                        except Exception, e:
                            logger.error("bitmhalo: message read: %s" %
                                         traceback.format_exc())
                        mymessage['toAddress'] = str(src1)
                        mymessage['fromAddress'] = str(src)
                        try:
                            body = str(body.encode('utf8'))
                        except:
                            logger.error("bitmhalo: not encoded")
                        try:
                            try:
                                body = body.split('****')[1].split('****')[0]
                            except:#In case the stars were removed
                                test = body
                                try:
                                    test = test.split('TheirBMAddress')[1].split('}')[0]
                                except:
                                    try:
                                        test = test.split('ENCRYPTED:')[1].split('\r\n')[0]
                                    except:
                                        float('a')
                        except:
                            try:
                                if 'You have received a payment of ' not in str(body):
                                    body = ""
                                else:
                                    # I'm hoping email providers will not change this as identifying the full base64 string would be challenging.
                                    # Any added padding gets changed when uploading the base64 image with the pyzmail library, although the bitmap is lossless
                                    body = \
                                        body.split(
                                            '<doge>\nContent-Disposition: inline\n\n')[1].split('\n--=========')[0]
                                    body = "PAY TO EMAIL BASE64 IMAGE:" + body
                            except Exception, _:
                                # Okay they changed it we can try something else
                                try:
                                    bodymsg = email.message_from_string(
                                        str(body))
                                    x = 0
                                    posx = 0
                                    while x < len(bodymsg.get_payload()):
                                        attachment = bodymsg.get_payload()[x]
                                        if "bmp" in attachment.get_content_type():
                                            posx = x
                                        x += 1
                                    attachment = msg.get_payload()[posx]
                                    img = attachment.get_payload(decode=False)
                                    body = img
                                    body = "PAY TO EMAIL BASE64 IMAGE:" + body
                                except Exception, e:
                                    logger.error("bitmhalo: parse: %s %s" %
                                                 (str(e), traceback.format_exc()))
                                    body = ""
                        if 'fromAddress' in mymessage and body != "":  # decode emails
                            if '@aol' in mymessage['fromAddress'].lower() or '@mail' in mymessage[
                                    'fromAddress'].lower():
                                body = body.encode('utf8').replace("\r\n ", "")
                                if "ENCRYPTED:" in body:
                                    body = body.replace(" ", "")
                        mymessage['body'] = str(body)
                        mymessage['uid'] = msg_id
                        if 'fromAddress' in mymessage and 'toAddress' in mymessage:
                            mailbox[str(dat['Email Address'])][msg_id] = ast.literal_eval(
                                str(mymessage))
                    if 'ordernumber' in dat:
                        if "ENCRYPTED:" in str(body):
                            try:
                                cipher_txt = body.replace("ENCRYPTED:", "")
                                cipher_txt = base64.b64decode(cipher_txt)
                                cipher_txt = decrypt(cipher_txt, dat['Private Key'])
                                body = cipher_txt
                            except Exception, e:
                                logger.error("bitmhalo: decrypt: %s %s" %
                                             (str(e), traceback.format_exc()))
                                try:
                                    body = body.replace("=\r\n", "")
                                    body = body.replace("\r\n", "")
                                    body = body.replace(" ", "")
                                    body = body.replace("****", "")

                                    try:
                                        body = body.encode('utf8')
                                    except Exception, e:
                                        logger.error("bitmhalo: encode utf8: %s %s" %
                                                     (str(e), traceback.format_exc()))

                                    try:
                                        cipher_txt = quopri.decodestring(body)
                                    except Exception, e:
                                        logger.error("bitmhalo: decodestring: %s %s" %
                                                     (str(e), traceback.format_exc()))
                                        cipher_txt = body

                                    cipher_txt = cipher_txt.replace("ENCRYPTED:", "")
                                    missing_padding = len(cipher_txt) % 4
                                    if missing_padding != 0:
                                        cipher_txt += b'=' * (4 - missing_padding)
                                    cipher_txt = base64.b64decode(cipher_txt)
                                    cipher_txt = decrypt(cipher_txt, dat['Private Key'])
                                    body = cipher_txt
                                except Exception, e:
                                    logger.error("bitmhalo: decrypt: %s %s" %
                                                 (str(e), traceback.format_exc()))

                        if dat['ordernumber'] in str(body):
                            try:
                                body = ast.literal_eval(body)
                                if body['ordernumber'] == dat['ordernumber']:
                                    connection.uid('STORE', msg_id, '+FLAGS',
                                                   '(\Deleted)')  # The flags should always be in parenthesis
                                    connection.expunge()
                                    logger.info(
                                        "bitmhalo: removed, msg_id: %s" % msg_id)
                                    try:
                                        mailbox[str(dat['Email Address'])].pop(
                                            msg_id)
                                    except Exception, e:
                                        logger.error("bitmhalo: not removed from cache, msg_id: %s, %s, %s" % (
                                            str(e), msg_id, traceback.format_exc()))
                            except Exception, e:
                                logger.error("bitmhalo: not removed: %s %s" %
                                             (str(e), traceback.format_exc()))
                        else:
                            logger.info(
                                "bitmhalo: not removed, msg_id: %s" % msg_id)
                    if mymessage not in inbox:
                        inbox.append(mymessage)
                # To save time and to avoid duplicates, i used to break at INBOX but we should also check Junk folder
                # if str(mailbox_name)=="INBOX":
                #   break
            except Exception, e:
                # Mailbox error
                logger.error("bitmhalo: inbox: %s %s" % (str(e), traceback.format_exc()))
                if shared.systemexit == 2:
                    sys.exit()
                pass
        logger.warning("bitmhalo: imap, closing.")
        connection.close()
        logger.warning("bitmhalo: imap, closed")
    except Exception, e:
        if shared.systemexit == 2:
            sys.exit()
        logger.error("bitmhalo: inbox: %s %s" % (str(e), traceback.format_exc()))
        readmessages = []
        ret = False

    return ret, readmessages, mailbox
