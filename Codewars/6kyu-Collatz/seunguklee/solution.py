def g_collatz(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield n


def collatz(n):
    return '->'.join(str(e) for e in g_collatz(n))

