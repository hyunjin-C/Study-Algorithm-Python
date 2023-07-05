def solution(babbling):
    answer = 0
    can_babbling = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for can_word in can_babbling:
            word = word.replace(can_word, '.')

        word = set(word)
        if word == {'.'}:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
