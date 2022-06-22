# 피보나치 수

import sys

# TopDown

d = [0] * 50


def fivo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fivo(x - 1) + fivo(x - 2)
    return d[x]


n = int(sys.stdin.readline())

print(fivo(n))


# BottomUp

n = int(sys.stdin.readline())

d = [0] * 100

d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
