import heapq


def solution(k, score):
    answer = []
    fame = []
    for i in score:
        heapq.heappush(fame, i)
        if (len(answer) >= k):
            heapq.heappop(fame)
        result = fame[0]
        answer.append(result)

    return answer


# [10, 10, 10, 20, 20, 100, 100]
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
