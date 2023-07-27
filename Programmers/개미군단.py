def solution(hp):
    answer = 0
    answer = hp // 5 + (hp % 5) // 3 + ((hp % 5) % 3)

    return answer


print(solution(23))  # 5 -> 장군(5)*4 + 병정(3)*1
print(solution(24))  # 6 -> 장군(5)*4 + 병정(3)*1 + 일(1)*1
print(solution(999))  # 201 -> 장군(5)*199 + 병정(3)*1 + 일(1)*!
