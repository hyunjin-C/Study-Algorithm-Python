from collections import deque

queue = deque()
n = int(input())

for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    p = queue.popleft()
    queue.append(p)

print(*queue)
