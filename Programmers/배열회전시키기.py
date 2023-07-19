from collections import deque

def solution(numbers, direction):
    answer = []
    numbers = deque(numbers)
    if direction == 'right':
        n = numbers.pop()
        answer.append(n)
        for i in numbers:
            answer.append(i)
    else:
        n = numbers.popleft()
        for i in numbers:
            answer.append(i)
        answer.append(n)
    
        
    
    return answer

print(solution([1, 2, 3], "right")) #  [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], "left")) #  [455, 6, 4, -1, 45, 6, 4]