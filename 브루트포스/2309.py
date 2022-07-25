import sys

input = sys.stdin.readline

dwarf = [int(input()) for _ in range(9)]
temp1, temp2 = 0, 0

for i in range(9):
    for j in range(i + 1, 9):
        if sum(dwarf) - (dwarf[i] + dwarf[j]) == 100:
            temp1 = dwarf[i]
            temp2 = dwarf[j]

dwarf.remove(temp1)
dwarf.remove(temp2)

print('\n'.join(map(str, sorted(dwarf))))
