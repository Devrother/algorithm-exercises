#!/bin/python3

N = int(input())

if N%2 == 1:
    print('Weird')
elif N > 1 and N < 6:
    print('Not Weird')
elif N > 5 and N < 21:
    print('Weird')
elif N > 20:
    print('Not Weird')