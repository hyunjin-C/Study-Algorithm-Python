import sys

T = int(input())

for _ in range(T):  # 테스트 개수만큼
    sentence = sys.stdin.readline().rstrip()  # 문장 입력 받기
    sentence += ' '  # 입력 받은 문자의 마지막에 공백을 추가하여 마지막 단어도 stack 리스트에서 꺼낼 수 있도록

    stack = list()

    for word in sentence:
        if word != ' ':
            stack.append(word)

        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
    print()
