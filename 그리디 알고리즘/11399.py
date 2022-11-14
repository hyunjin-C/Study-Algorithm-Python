import sys
input = sys.stdin.readline


n = int(input())
time = list(map(int, input().split()))
p = 0
sum = 0

time.sort()

for i in range(n):
    p = 0
    for j in range(0, i + 1):
        p += time[j]
    sum += p

print(sum)
