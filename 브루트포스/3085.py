import sys

input = sys.stdin.readline


def check(board):
    n = len(board)
    answer = 1

    # 열 순회하면서 연속되는 숫자 세기
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            # 이전과 같다면
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            # 이전과 다르다면
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt

    # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt

    return answer


n = int(input())
board = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

            temp = check(board)

            if temp > answer:
                answer = temp

            # 바꾼 것을 다시 원래대로 돌려놓기
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 행 바꾸기
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

            temp = check(board)

            if temp > answer:
                answer = temp

            # 바꾼 것을 다시 원래대로 돌려놓기
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)
