def josephus(items, k):
    return [e for e in joesphus_gen(items, k)]


def joesphus_gen(items, k):
    now = 0
    while items:
        now = next_step(now, len(items), k-1)
        yield items[now]
        del items[now]

def next_step(now, lenght, count):
    return (now + count) % lenght