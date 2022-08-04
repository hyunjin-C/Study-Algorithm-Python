n = int(input())
binary = ''

if n == 0:
    print(0)

while n:  # n이 0이 될 때까지
    if n % -2:  # 나머지가 -1이나 1일 때
        binary = binary + '1'
        n = n // -2 + 1
    else:  # 나머지가 0일 때
        binary = binary + '0'
        n = n // -2

print(binary[::-1])
