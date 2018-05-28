#!/usr/bin/python

n = int(input())

index = {1: True, 2: True}
p, k = 2, 2
res = []


while k <= 10000000000:
    k += p
    index[k] = True
    p += 1

for _ in range(n):
    i = int(input())
    res.append('1' if index.get(i) else '0')

print(' '.join(res))
