import sys

d = [0] * 10001


def RectangleCount(x):
    d[1] = 1
    d[2] = 2

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]


n = int(sys.stdin.readline())

print(RectangleCount(n) % 10007)
