import sys

input = sys.stdin.readline

d = [0] * 100001


def rectangle_count(x):
    d[1] = 1
    d[2] = 3

    for i in range(3, x + 1):
        d[i] = d[i - 1] + (d[i - 2] * 2)

    return d[x]


n = int(input())

print(rectangle_count(n) % 10007)
