print()
for i in range(3):
    print(" ", end="")
print("Merry Christmas\n")

for i in range(9):
    print(' ', end="")
print('⭐')

for i in range(1, 11):
    for j in range(1, 11 - i + 1):
        print(' ', end="")
    for k in range(1, 2 * i):
        print('▲', end="")
    print()

for i in range(1, 3):
    for j in range(1, 9):
        print(" ", end="")
    for k in range(1, 6):
        print("▮", end="")
    print()

for i in range(23):
    print("~", end="")
print()

#     print("🎁", end="")
