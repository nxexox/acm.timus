a = int(input())

result = None
if 1 <= a <= 4:
    result = "few"
elif 5 <= a <= 9:
    result = "several"
elif 10 <= a <= 19:
    result = "pack"
elif 20 <= a <= 49:
    result = "lots"
elif 50 <= a <= 99:
    result = "horde"
elif 100 <= a <= 249:
    result = "throng"
elif 250 <= a <= 499:
    result = "swarm"
elif 500 <= a <= 999:
    result = "zounds"
else:
    result = "legion"

print(result)
