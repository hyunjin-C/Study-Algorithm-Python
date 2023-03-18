def productExceptSelf(nums):
    answer = []
    p, q = 1, 1
    # 자기 자신 제외한 왼쪽 값 곱하기
    for i in range(len(nums)):
        answer.append(p)
        p = p * nums[i]
    # 자기 자신 제외한 오른쪽 값 곱하기
    for j in range(len(nums) - 1, -1, -1):
        answer[j] = answer[j] * q
        q = q * nums[j]

    return answer
