#!/usr/bin/python

n = int(input())


px = [0, 1, 1, 2, 2, -1, -1, -2, -2]
py = [0, 2, -2, 1, -1, 2, -2, 1, -1]


for _ in range(n):
    string = input()
    ch, c = string[0], int(string[1])
    b = ord(ch) - ord('a') + 1
    ans = 0
    for j in range(1, 9):
        if 0 < b + px[j] <= 8 and 0 < c + py[j] <= 8:
            ans += 1

    print(ans)
