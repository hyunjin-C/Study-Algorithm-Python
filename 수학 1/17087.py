import sys
import math

input = sys.stdin.readline
a = []
result = []

n, s = map(int, input().split())

a = list(map(int, input().split()))

for i in range(n):
    result.append(abs(s - a[i]))

print(math.gcd(*result))
