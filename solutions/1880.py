#!/usr/bin/python

index = {}
count = 0

input()
for i in input().split():
    x = int(i)
    index[x] = 1

input()
for i in input().split():
    x = int(i)
    index.setdefault(x, 0)
    index[x] += 1

input()
for i in input().split():
    x = int(i)
    index.setdefault(x, 0)
    index[x] += 1
    if index[x] == 3:
        count += 1

print(count)
