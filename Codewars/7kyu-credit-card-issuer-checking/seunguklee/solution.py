from collections import namedtuple

IssuerInfo = namedtuple('IssuerInfo', 'begins, lengths')

ISSUERS = {
    IssuerInfo(('34', '37'), (15,)): 'AMEX',
    IssuerInfo(('6011',), (16,)): 'Discover',
    IssuerInfo(('51', '52', '53', '54', '55'), (16,)): 'Mastercard',
    IssuerInfo(('4'), (13, 16)): 'VISA',
}

def get_issuer(number):
    str_n = str(number)
    return next((card for (begins, lengths), card in ISSUERS.items()
        if str_n.startswith(begins) and len(str_n) in lengths), 'Unknown')