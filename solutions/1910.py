#!/urs/bin/python

input()

_max, index = 0, 0

array = [int(i) for i in input().split()]

for i in range(1, len(array) - 1):
    c = array[i] + array[i - 1] + array[i + 1]
    if c > _max:
        _max = c
        index = i + 1

print(_max, index)
