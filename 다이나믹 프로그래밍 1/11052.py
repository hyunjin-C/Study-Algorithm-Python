n = int(input())  # 민규가 구매하려는 카드의 개수
d = [0] * (n + 1)  # n개의 카드 사는 경우의 수
p = [0] + list(map(int, input().split()))  # n개의 카드팩 가격 p[1]부터 입력받음

d[1] = p[1]  # 1개 사면 최대값 p[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + p[j])
print(d[i])
