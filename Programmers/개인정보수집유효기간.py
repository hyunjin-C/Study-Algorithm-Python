def solution(today, terms, privacies):
    answer = []
    terms_dic = {}

    today_year, today_month, today_day = today.split('.')
    today_year, today_month, today_day = int(
        today_year), int(today_month), int(today_day)

    for i in range(len(terms)):
        terms_dic[terms[i][0]] = int(terms[i][2:])

    for i in range(len(privacies)):
        type = privacies[i][-1]
        privacies_year, privacies_month, privacies_day = privacies[i][:-2].split(
            '.')
        privacies_year, privacies_month, privacies_day = int(
            privacies_year), int(privacies_month), int(privacies_day)

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
