import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if array[i - 1] < array[i]:
        for j in range(n - 1, 0, -1):
            if array[i - 1] < array[j]:
                array[i - 1], array[j] = array[j], array[i - 1]
                array = array[:i] + sorted(array[i:])
                print(*array)
                exit()
print(-1)
