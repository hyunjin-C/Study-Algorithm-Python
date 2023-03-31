import itertools
from collections import deque

n, m = map(int, input().split())
basket = deque()

for x in range(1, n + 1):
    basket.append(x)

for _ in range(m):
    i, j, k = map(int, input().split())
    slice_basket = deque(itertools.islice(basket, i - 1, k - 1))
    for _ in range(len(slice_basket)):
        tmp = slice_basket.popleft()
        basket.remove(tmp)
        basket.insert(j - 1, tmp)

print(*basket)
