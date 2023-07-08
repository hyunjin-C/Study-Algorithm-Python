def calculator(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    else:
        if n1 == n2:
            return 'O'
        else:
            return 'X'


def solution(quiz):
    answer = []
    for problem in quiz:
        problem = problem.split(' ')
        num, operator = [], []

        for i, my_str in enumerate(problem):
            if i % 2 == 0:
                num.append(int(my_str))
            else:
                operator.append(my_str)

        tmp = num[0]
        for i in range(len(operator)):
            tmp = calculator(tmp, num[i+1], operator[i])

        answer.append(tmp)
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))  # ["X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
# ["O", "O", "X", "O"]
