from functools import reduce
from collections import Counter
from operator import mul

def solution(clothes):
    clothes_counter = get_clothes_counter(clothes)
    return get_cnt_combined_clothes(clothes_counter)


def get_clothes_counter(clothes):
    return Counter([kind for _, kind in clothes])


def get_cnt_combined_clothes(clothes):
    clothes_cnt_gen = (cnt for cnt in clothes.values())
    add_one = lambda x: x + 1
    return reduce(mul, map(add_one, clothes_cnt_gen)) - 1
