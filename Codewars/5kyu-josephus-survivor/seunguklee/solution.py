def josephus_survivor(n, k):
    jg = joesphus_gen(list(range(1, n + 1)), k)
    res = 0
    for e in jg:
        res = e
    return res

def joesphus_gen(items, k):
    now = 0
    while items:
        now = next_step(now, len(items), k-1)
        yield items[now]
        del items[now]


def next_step(now, lenght, count):
    return (now + count) % lenght