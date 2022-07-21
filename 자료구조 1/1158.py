import sys

input = sys.stdin.readline

n, k = map(int, input().split())
circle = []
result = []

for i in range(1, n + 1):
    circle.append(i)

temp = k - 1

for _ in range(n):
    if len(circle) > temp:
        result.append(circle.pop(temp))
        temp += k - 1

    else:
        temp = temp % len(circle)
        result.append(circle.pop(temp))
        temp += k - 1

print('<', end='')
print(*result, sep=', ', end='')
print('>')
