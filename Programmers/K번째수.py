def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice_array = array[i-1:j]
        slice_array.sort()
        answer.append(slice_array[k-1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [
      [2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
