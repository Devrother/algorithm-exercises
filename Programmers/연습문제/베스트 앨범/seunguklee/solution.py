from collections import defaultdict
# import bisect

"""
`d = {
        "classic": [(3, 800), (0, 500), (2, 150)],
        "genres": [], ...
    }`
이런식으로 만들어 `rank_d = sorted(((sum(p for p, i in value), key)
                     for key, value in d.items()), reverse=True)`
를 통해 `[(3100, 'pop'), (1450, 'classic')]` 같은 형태로 만든다
rank_d 를 순회하면서 우리가 원하는 베스트 앨범을 만들면 된다.

"""

def gen_c():
    i = 0
    while True:
        yield i
        i += 1


# def insert(list, n):
#     bisect.insort(list, n)
#     return list


def solution(genres, plays):
    d, answer = defaultdict(list), []
    
    for i, genre, play in zip(gen_c(), genres, plays):
        d[genre].append((play, i))
        # insert(d[genre], (play, i))

    for _, value in d.items():
        value.sort(key=lambda p: p[0], reverse=True)

    rank_d = sorted(((sum(p for p, i in value), key)
                     for key, value in d.items()), reverse=True)

    # print(rank_d)
    # print(d)

    for _, genre in rank_d:
        answer += [i for _, i in d[genre][:2]]
    return answer