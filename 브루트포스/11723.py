import sys

m = int(input())
s = set()

for _ in range(m):
    tmp = sys.stdin.readline().rstrip().split()

    # command만 있을 경우
    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    # command와 x가 존재할 때
    else:
        command, x = tmp[0], tmp[1]
        x = int(x)

        if command == 'add':
            s.add(x)
        elif command == 'remove':
            s.discard(x)
        elif command == 'check':
            print(1 if x in s else 0)
        elif command == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
