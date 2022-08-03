import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deque_list = deque()

for i in range(n):
    tmp = input().rstrip().split()
    if len(tmp) == 1:
        command = tmp[0]
        if command == 'pop_front':
            if deque_list:
                print(deque_list.popleft())
            else:
                print(-1)
        elif command == 'pop_back':
            if deque_list:
                print(deque_list.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(deque_list))
        elif command == 'empty':
            if not deque_list:
                print(1)
            else:
                print(0)
        elif command == 'front':
            if deque_list:
                print(deque_list[0])
            else:
                print(-1)
        else:
            if deque_list:
                print(deque_list[-1])
            else:
                print(-1)
    else:
        command, x = tmp[0], tmp[1]
        if command == 'push_front':
            deque_list.insert(0, x)
        else:
            deque_list.append(x)
