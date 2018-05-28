#!/usr/bin/python

n = int(input())

res, count = 0, 2

for _ in range(n):
    name = input()
    if name.endswith('+one'):
        count += 2
    else:
        count += 1

if count == 13:
    count += 1

print(count * 100)
