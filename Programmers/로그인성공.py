def solution(id_pw, db):
    answer = ''
    db_dic = dict(db)

    id, pw = id_pw[0], id_pw[1]

    if db_dic.get(id) == None:
        answer = 'fail'
    else:
        if (pw == db_dic[id]):
            answer = 'login'
        else:
            answer = 'wrong pw'

    return answer


print(solution(["meosseugi", "1234"], [["rardss", "123"],
      ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], [
      "programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"],
      ["krong0313", "29440"], ["rabbit00", "111333"]]))
