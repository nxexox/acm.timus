#!/usr/bin/python

n, k = [int(i) for i in input().split()]

# TODO: Сама система не принимает на 16-м тесте


def function(n, k):
    return round(float(n) * 2.0 / float(k)) if k < n else 2

print(function(n, k))
