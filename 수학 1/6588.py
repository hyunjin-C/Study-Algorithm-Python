import sys

prime_list = [True for i in range(1000001)]

for i in range(2, int(1000000**0.5) + 1):
    for j in range(i + i, 1000001, i):
        prime_list[j] = False

while True:
    n = int(sys.stdin.readline())

    if (n == 0):
        break

    for i in range(3, len(prime_list)):
        if prime_list[i] and prime_list[n - i]:
            print(n, "=", i, "+", n - i)
            break
