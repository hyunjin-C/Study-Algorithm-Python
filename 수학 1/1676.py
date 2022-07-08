from math import factorial

n = int(input())
count = 0

n = str(factorial(n))

# 뒤에서부터 체크
i = -1
while (i >= -len(n)):
    if n[i] == '0':
        count += 1
        i -= 1
    else:
        break

print(count)
