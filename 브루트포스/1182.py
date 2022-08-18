import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
number = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    result = list(combinations(number, i))
    for num in result:
        if (sum(num) == s):
            count += 1

print(count)
