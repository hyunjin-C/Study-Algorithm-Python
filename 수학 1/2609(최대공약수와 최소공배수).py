# 유클리드 호제법 이용

num1, num2 = map(int, input().split())


def GCD(x, y):
    while y > 0:
        x, y = y, x % y

    return x


def LCM(x, y):
    return x * y // GCD(x, y)


print(GCD(num1, num2))
print(LCM(num1, num2))
