#!/usr/bin/python
# Простая имитация автомата.
MATRIX = {
    1: {1: 0, 2: 1, 3: 2},
    2: {1: 1, 2: 0, 3: 1},
    3: {1: 2, 2: 1, 3: 0}
}

BOXES = {
    'Alice': 1, 'Ariel': 1, 'Aurora': 1, 'Phil': 1, 'Peter': 1, 'Olaf': 1, 'Phoebus': 1, 'Ralph': 1, 'Robin': 1,
    'Bambi': 2, 'Belle': 2, 'Bolt': 2, 'Mulan': 2, 'Mowgli': 2, 'Mickey': 2, 'Silver': 2, 'Simba': 2, 'Stitch': 2,
    'Dumbo': 3, 'Genie': 3, 'Jiminy': 3, 'Kuzko': 3, 'Kida': 3, 'Kenai': 3, 'Tarzan': 3, 'Tiana': 3, 'Winnie': 3
}

n = int(input())
now = 1
res = 0

for _ in range(n):
    name = input()
    box = BOXES.get(name)
    res += MATRIX[now][box]
    now = box

print(res)
