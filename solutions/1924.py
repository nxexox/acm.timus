#!/usr/bin/python

n = int(input())


def game(n):
    res = 0
    if n == 1:
        return 'grimy'

    if n % 2 == 0:
        res = n / 2
    else:
        res = n / 2 + 1
    if res % 2 == 0:
        return 'black'
    else:
        return 'grimy'

print(game(n))
