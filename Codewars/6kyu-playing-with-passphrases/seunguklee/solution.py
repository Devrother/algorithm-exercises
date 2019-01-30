def shift_letter(c, n):
    shifted = chr((ord(c) + n))
    if 'Z' < shifted or shifted > 'z':
        return chr(ord(shifted) - 26)

    return shifted


def nine_complementary_number(n):
    return str(9 - int(n)) if n.isdigit() else n


def lowwer_or_upper(c, i):
    return c.lower() if i % 2 == 1 else c.upper()


def play_pass(s, n):
    res = [lowwer_or_upper(shift_letter(c, n), i) if c.isalpha() else nine_complementary_number(c) for i, c in enumerate(s)]
    return (''.join(res))[::-1]

