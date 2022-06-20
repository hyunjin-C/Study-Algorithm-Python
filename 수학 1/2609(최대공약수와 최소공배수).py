# 단순 수식으로 구하기

num1, num2 = map(int, input().split())


def GCD(x, y):
    for i in range(1, min(x, y) + 1):
        if ((x % i == 0) and (y % i == 0)):
            result = i

    return result


def LCM(x, y):
    return x * y // GCD(x, y)


print(GCD(num1, num2))
print(LCM(num1, num2))
