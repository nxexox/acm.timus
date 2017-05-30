# coding: utf8
# 1787. Поворот на МЕГУ

k, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

stack = 0
for i in a:
    stack += i
    if stack > 0:
        stack -= k
    if stack < 0:
        stack = 0

print(stack)
