import sys
from collections import deque
input = sys.stdin.readline


def solution(n, tree):
    q = deque([1])
    parent = [0] * (n + 1)
    while q:
        now = q.popleft()
        for i in tree[now]:
            if parent[i] == 0 and i != 1:
                parent[i] = now
                q.append(i)
    for i in range(2, n + 1):
        print(parent[i])


n = int(input())
tree = dict()  # 딕셔너리 사용(이중리스트로도 가능)

for i in range(1, n + 1):
    tree[i] = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

solution(n, tree)
