def solution(spell, dic):
    answer = 0
    for i, dic_word in enumerate(dic):
        word = []
        dic_word = list(set(dic_word))
        for dic_spell in dic_word:
            if dic_spell in spell:
                word.append(dic_spell)
        if len(word) == len(spell):
            answer = 1
            break
        elif i == len(dic) - 1:
            answer = 2

    return answer


print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))  # 2
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))  # 1
print(solution(["s", "o", "m", "d"], [
      "moos", "dzx", "smm", "sunmmo", "som"]))  # 2
