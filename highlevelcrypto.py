from binascii import hexlify

import pyelliptic
from pyelliptic import OpenSSL
from pyelliptic import arithmetic as a


def makeCryptor(privkey):
    private_key = a.changebase(privkey, 16, 256, minlen=32).encode("latin1")
    public_key = pointMult(private_key)
    privkey_bin = b"\x02\xca\x00\x20" + private_key
    pubkey_bin = b"\x02\xca\x00\x20" + public_key[1:-32] + b"\x00\x20" + public_key[-32:]
    cryptor = pyelliptic.ECC(curve="secp256k1", privkey=privkey_bin, pubkey=pubkey_bin)
    return cryptor


def hexToPubkey(pubkey):
    pubkey_raw = a.changebase(pubkey[2:], 16, 256, minlen=64).encode("latin1")
    pubkey_bin = b"\x02\xca\x00\x20" + pubkey_raw[:32] + b"\x00\x20" + pubkey_raw[32:]
    return pubkey_bin


def makePubCryptor(pubkey):
    pubkey_bin = hexToPubkey(pubkey)
    return pyelliptic.ECC(curve="secp256k1", pubkey=pubkey_bin)


# Converts hex private key into hex public key
def privToPub(privkey):
    private_key = a.changebase(privkey, 16, 256, minlen=32).encode("latin1")
    public_key = pointMult(private_key)
    return hexlify(public_key).decode()


# Encrypts message with hex public key
def encrypt(msg, hexPubkey):
    return pyelliptic.ECC(curve="secp256k1").encrypt(msg, hexToPubkey(hexPubkey))


# Decrypts message with hex private key
def decrypt(msg, hexPrivkey):
    return makeCryptor(hexPrivkey).decrypt(msg)


# Decrypts message with an existing pyelliptic.ECC.ECC object
def decryptFast(msg, cryptor):
    return cryptor.decrypt(msg)


# Signs with hex private key
def sign(msg, hexPrivkey):
    # Upgrading from SHA1 to SHA256
    try:
        return makeCryptor(hexPrivkey).sign(msg, digest_alg=OpenSSL.EVP_sha256)
    except:
        return makeCryptor(hexPrivkey).sign(msg, digest_alg=OpenSSL.digest_ecdsa_sha1)


# Verifies with hex public key
def verify(msg, sig, hexPubkey):
    try:
        if makePubCryptor(hexPubkey).verify(sig, msg, digest_alg=OpenSSL.EVP_sha256):
            return True
    except Exception as e:
        # print(f"Verify SHA256 failed: {e}")
        pass

    try:
        # print("Trying SHA1 verify.")
        if makePubCryptor(hexPubkey).verify(sig, msg, digest_alg=OpenSSL.digest_ecdsa_sha1):
            return True
    except Exception as e2:
        # print(f"Verify SHA1 failed: {e2}")
        pass

    return False


# Does an EC point multiplication; turns a private key into a public key.
def pointMult(secret):
    try:
        k = OpenSSL.EC_KEY_new_by_curve_name(OpenSSL.get_curve("secp256k1"))
        priv_key = OpenSSL.BN_bin2bn(secret, 32, None)
        group = OpenSSL.EC_KEY_get0_group(k)
        pub_key = OpenSSL.EC_POINT_new(group)

        OpenSSL.EC_POINT_mul(group, pub_key, priv_key, None, None, None)
        OpenSSL.EC_KEY_set_private_key(k, priv_key)
        OpenSSL.EC_KEY_set_public_key(k, pub_key)

        size = OpenSSL.i2o_ECPublicKey(k, None)
        mb = OpenSSL.create_string_buffer(size)
        OpenSSL.i2o_ECPublicKey(k, OpenSSL.byref(OpenSSL.pointer(mb)))

        OpenSSL.EC_POINT_free(pub_key)
        OpenSSL.BN_free(priv_key)
        OpenSSL.EC_KEY_free(k)
        return mb.raw

    except Exception as e:
        import traceback

        traceback.print_exc()
        raise
