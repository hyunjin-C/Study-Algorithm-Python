# 가위 : 2, 바위: 0, 보: 5

def solution(rsp):
    answer = ''
    rsp_game = {'2': '0', '0': '5', '5': '2'}

    for x in rsp:
        answer += rsp_game[x]

    return answer


print(solution('2'))  # '0'
print(solution('205'))  # '052'
