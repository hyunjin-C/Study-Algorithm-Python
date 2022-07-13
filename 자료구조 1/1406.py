import sys

input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list()
m = int(input())

for _ in range(m):
    command = list(input().split())

    if command[0] == 'L':
        if str1:
            str2.append(str1.pop())

    elif command[0] == 'D':
        if str2:
            str1.append(str2.pop())

    elif command[0] == 'B':
        if str1:
            str1.pop()

    else:
        str1.append(command[1])

print(''.join(str1 + list(reversed(str2))))
