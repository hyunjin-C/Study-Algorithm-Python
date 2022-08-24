import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


def dfs(start, depth):

    visited[start] = True  # 해당 노드 방문 체크

    # 해당 시작점을 기준으로 계속 dfs로 그래프를 탐색한다.
    for i in graph[start]:
        if not visited[i]:  # 방문하지 않았다면
            dfs(i, depth + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs 탐색
            count += 1

print(count)
