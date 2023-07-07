def calculator(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    else:
        return n1 - n2


def solution(my_string):
    answer = 0

    my_string = my_string.split(' ')
    num, operator = [], []

    for i, my_str in enumerate(my_string):
        if i % 2 == 0:
            num.append(int(my_str))
        else:
            operator.append(my_str)

    tmp = num[0]

    for i in range(len(operator)):
        tmp = calculator(tmp, num[i+1], operator[i])

    answer = tmp

    return answer


print(solution("3 + 4"))  # 7
print(solution("3 + 4 - 2"))  # 5
print(solution("3 + 4 - 2 + 10"))  # 15
