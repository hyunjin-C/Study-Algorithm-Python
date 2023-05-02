def recursion(s, l, r, cnt):
    cnt += 1
    if (l >= r):
        print(1, cnt)
    elif (s[l] != s[r]):
        print(0, cnt)
    else:
        return recursion(s, l + 1, r - 1, cnt)


def isPalindrome(s, cnt):
    return recursion(s, 0, len(s) - 1, cnt)


T = int(input())
cnt = 0
for _ in range(T):
    s = input()
    isPalindrome(s, cnt)
