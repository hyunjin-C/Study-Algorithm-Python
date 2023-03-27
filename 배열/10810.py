n, m = map(int, input().split())
basket = {}

for x in range(n):
    basket[x] = 0

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        basket[x] = k

for x in basket:
    print(basket[x], end=" ")
