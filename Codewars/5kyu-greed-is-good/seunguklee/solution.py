from collections import Counter


def check(c):
    a, b = c // 3, c % 3
    return [3] * a + [1] * b


def score(dice):
    score_map = {
        (1, 3): 1000,
        (6, 3): 600,
        (5, 3): 500,
        (4, 3): 400,
        (3, 3): 300,
        (2, 3): 200,
        (1, 1): 100,
        (5, 1): 50
    }

    return sum(score_map[(n, k)]
               for n, c in Counter(dice).items()
               for k in check(c)
               if (n, k) in score_map)