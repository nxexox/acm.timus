#!/usr/bin/python

a, b = [int(i) for i in input().split()]
c = a * b

if c % 2 == 0:
    print('[:=[first]')
else:
    print('[second]=:]')
