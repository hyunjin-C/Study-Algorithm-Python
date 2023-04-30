# 반복문으로 한 줄에 하나씩 pop해서 새로운 리스트에 push
from collections import deque

word_list = list(list(input() for _ in range(5)))
answer = []
cnt = []

for i in range(5):
    word_list[i] = deque(word_list[i])
    cnt.append(len(word_list[i]))

i = 0
max = max(cnt)
cycle = 0

while True:
    if word_list[i]:
        word = word_list[i].popleft()
        answer.append(word)
    elif (cycle == max and i == 4):
        break

    i += 1
    if i > 4:
        i = 0
        cycle += 1


print(''.join(answer))
