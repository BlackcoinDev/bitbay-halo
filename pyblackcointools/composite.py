from .bci import pushtx, unspent
from .main import privtoaddr
from .transaction import mksend, select, signall


# Takes privkey, address, value (satoshis), fee (satoshis)
def send(frm, to, value, fee=1000):
    u = unspent(privtoaddr(frm))
    u2 = select(u, value + fee)
    argz = u2 + [to + ":" + str(value)] + [privtoaddr(frm), fee]
    tx = mksend(*argz)
    tx2 = signall(tx, frm)
    return pushtx(tx2)
