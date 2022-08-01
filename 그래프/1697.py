from collections import deque


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()  # 시작점
        if x == k:
            print(visited[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)


MAX = 10 ** 5
visited = [0] * (MAX + 1)  # 이동하는 거리 표현
n, k = map(int, input().split())

bfs()
