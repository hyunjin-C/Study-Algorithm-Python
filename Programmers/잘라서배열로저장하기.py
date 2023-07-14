def solution(my_str, n):
    answer = []
    tmp = ''
    for i, arr in enumerate(my_str):
        tmp += arr
        if (i + 1) % n == 0 or i == len(my_str) - 1:
            answer.append(tmp)
            tmp = ''

    return answer


print(solution("abc1Addfggg4556b", 6))  # ["abc1Ad", "dfggg4", "556b"]
print(solution("abcdef123", 3))  # ["abc", "def", "123"]
