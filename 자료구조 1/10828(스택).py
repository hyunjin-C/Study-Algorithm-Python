import sys

n = int(sys.stdin.readline())
stack_list = list()

for i in range(n):
    command_n = sys.stdin.readline()

    if "push" in command_n:
        num = int(command_n[4:])
        stack_list.append(num)

    elif "pop" in command_n:
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())

    elif "size" in command_n:
        print(len(stack_list))

    elif "empty" in command_n:
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)

    elif "top" in command_n:
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[len(stack_list) - 1])
