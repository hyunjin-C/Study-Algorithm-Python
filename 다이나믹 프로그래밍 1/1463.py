# 1로 만들기

import sys

n = int(sys.stdin.readline())

d = [0] * 1000001

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1  # 1을 뺀 경우

    if i % 3 == 0:  # 3으로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 2 == 0:  # 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])
