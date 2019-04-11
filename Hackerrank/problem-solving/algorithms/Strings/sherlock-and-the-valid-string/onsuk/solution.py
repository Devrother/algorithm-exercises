#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    counted_sorted_s = sorted(list(collections.Counter(s).values()))
    print(counted_sorted_s)
    if counted_sorted_s.count(counted_sorted_s[0]) == len(counted_sorted_s):
        return 'YES'
    elif (counted_sorted_s.count(counted_sorted_s[0]) == len(counted_sorted_s) - 1) and counted_sorted_s[-1] - \
            counted_sorted_s[-2] == 1:
        return 'YES'
    elif (counted_sorted_s.count(counted_sorted_s[-1]) == len(counted_sorted_s) - 1) and counted_sorted_s[0] == 1:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
