#!/usr/bin/python

n = int(input())

matrix = []
res = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(2 * n):
    for j in range(n):
        if 0 <= i - j < n:
            res.append(matrix[i - j][j])

print(' '.join(map(str, res)))
