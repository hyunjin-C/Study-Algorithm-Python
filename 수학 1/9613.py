import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sum_gcd = 0
    num = list(map(int, input().split()))

    n = num[0]
    for i in range(1, n):
        for j in range(2, n + 1):
            if i < j:
                sum_gcd += math.gcd(num[i], num[j])

    print(sum_gcd)
