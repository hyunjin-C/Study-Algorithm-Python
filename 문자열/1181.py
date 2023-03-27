import sys

input = sys.stdin.readline

N = int(input())
words = []

# 단어 입력
for i in range(N):
    words.append(input().rsplit())

# 단어의 중복을 없애기 위해 set 자료형으로 값 저장 후 리스트로 변환(안덱싱으로 접근하기 위해)
set_word = list(set(words))

for i in set_word:
    print(i)
