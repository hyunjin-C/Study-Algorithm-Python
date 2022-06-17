import sys

T = int(input())

for _ in range(T):  # 테스트 개수만큼
    stack = list()

    ps = sys.stdin.readline().rstrip()  # 괄호 입력 받음
    cnt = 0  # 괄호 판단

    for i in ps:
        if i == '(':
            stack.append(i)
            cnt += 1

        else:
            cnt -= 1
            if cnt == -1:
                break

            if len(stack) != 0:
                stack.pop()

    if cnt == 0:
        print("YES")
    else:
        print("NO")
