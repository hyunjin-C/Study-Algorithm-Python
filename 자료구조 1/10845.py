import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue_list = deque([])

for _ in range(n):
    command = input()

    if 'push' in command:
        num = command[5:]
        queue_list.append(num)

    if 'pop' in command:
        if queue_list:
            print(queue_list.popleft(), end='')
        else:
            print(-1)

    if 'size' in command:
        print(len(queue_list))

    if 'empty' in command:
        if queue_list:
            print(0)
        else:
            print(1)

    if 'front' in command:
        if queue_list:
            print(queue_list[0], end='')
        else:
            print(-1)

    if 'back' in command:
        if queue_list:
            print(queue_list[-1], end='')
        else:
            print(-1)
