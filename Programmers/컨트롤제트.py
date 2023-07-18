# 풀이 1) 문자열 사용
def cal(a, b, c):
    if b == 'Z':
        a, c = int(a), int(c)
        return a - c
    else:
        a, b = int(a), int(b)
        return a + b


def solution1(s):
    answer = 0
    s = s.split(' ')

    for i in range(len(s)):
        if i == 0:
            answer = cal(answer, s[i], 0)

        elif i > 0:
            answer = cal(answer, s[i], s[i-1])
    return answer


# 풀이 2) 스택 사용
def solution2(s):
    answer = 0
    s_list = []
    s = s.split(' ')

    for i in s:
        if s_list and i == 'Z':
            s_list.pop()
        else:
            s_list.append(int(i))

    for j in s_list:
        answer += j

    return answer


print(solution1("1 2 Z 3"))  # 4
print(solution1("10 20 30 40"))  # 100
print(solution2("10 Z 20 Z 1"))  # 1
print(solution2("10 Z 20 Z"))  # 0
print(solution2("-1 -2 -3 Z"))  # -3
