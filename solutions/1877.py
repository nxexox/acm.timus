a = int(input())
b = int(input())
buf = "no"
for i in range(9999):
    if i % 2:
        if b == i:
            buf = "yes"
    else:
        if a == i:
            buf = "yes"
    if buf != "no":
        break
print(buf)