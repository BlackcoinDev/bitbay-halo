from .bci import unspent, pushtx
from .main import privtoaddr
from .transaction import select, mksend, signall

# Takes privkey, address, value (satoshis), fee (satoshis)
def send(frm,to,value,fee=1000):
    u = unspent(privtoaddr(frm))
    u2 = select(u,value+fee)
    tx = mksend(to+':'+str(value),privtoaddr(to),fee)
    tx2 = signall(tx,privtoaddr(to))
    pushtx(tx)
