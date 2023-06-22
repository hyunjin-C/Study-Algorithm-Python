def solution(today, terms, privacies):
    answer = []
    terms_dic = {}

    today_year, today_month, today_day = map(int, today.split('.'))

    for i in range(len(terms)):
        terms_dic[terms[i][0]] = int(terms[i][2:])

    for i in range(len(privacies)):
        type = privacies[i][-1]
        privacies_year, privacies_month, privacies_day = map(
            int, privacies[i][:-2].split('.'))

        privacies_month += terms_dic[type]

        if privacies_month > 12:
            privacies_year += privacies_month // 12
            privacies_month = privacies_month % 12
            if privacies_month == 0:
                privacies_year -= 1
                privacies_month = 12

        if today_year > privacies_year:
            answer.append(i+1)
        elif (today_year == privacies_year):
            if today_month > privacies_month:
                answer.append(i+1)
            elif (today_month == privacies_month):
                if today_day >= privacies_day:
                    answer.append(i+1)
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], [
      "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

print(solution("2020.01.01", ["Z 3", "D 5"], [
      "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

print(solution("2021.12.08", ["A 18"], ["2020.06.18 A"]))
