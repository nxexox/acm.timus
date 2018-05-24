#!/usr/bin/python

a, b, c = int(input()), int(input()), int(input())

res = a * b * c + a + b + c

res = min(res, a + b + c)
res = min(res, a + b - c)
res = min(res, a + b * c)
res = min(res, a - b + c)
res = min(res, a - b - c)
res = min(res, a - b * c)
res = min(res, a * b + c)
res = min(res, a * b - c)
res = min(res, a * b * c)

print(res)
