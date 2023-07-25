# deque 이용한 bfs
from collections import deque


def solution1(numbers, target):
    answer = 0
    queue = deque()
    numbers = deque(numbers)

    num = numbers.popleft()
    queue.append(num)
    queue.append(num * -1)

    for num in numbers:
        n = len(queue)
        for _ in range(n):
            tmp = queue.popleft()
            queue.append(tmp + num)
            queue.append(tmp - num)

    answer = queue.count(target)

    return answer


# 재귀함수 이용
def solution2(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer


print(solution1([1, 1, 1, 1, 1], 3))  # 5
print(solution2([4, 1, 2, 1], 4))  # 2
