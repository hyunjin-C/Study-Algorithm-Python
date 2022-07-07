import sys

input = sys.stdin.readline

n = int(input())

count = 0  # 스택에 넣을 숫자
result_list = []
stack = []
result = True

for i in range(n):
    x = int(input())  # 수열 입력

    while count < x:  # 입력한 숫자(x)보다 작은 숫자일 때
        count += 1
        stack.append(count)  # push
        result_list.append('+')

    if stack[-1] == x:  # 스택에서 가장 최근에 넣은 숫자가 입력한 숫자와 동일할 때
        stack.pop()  # pop
        result_list.append('-')
    else:
        result = False
        break

# 출력
if result == False:
    print("NO")
else:
    print("\n".join(result_list))
