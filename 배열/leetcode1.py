def twoSum(nums, target):
    # for i in range(len(nums) - 1):
    #     for j in range(1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return i, j

    # for i, num1 in enumerate(nums):
    #     num2 = target - num1
    #     if num2 in nums[i+1:]:
    #         return [nums.index(num1), nums[i+1:].index(num2) + (i + 1)]

    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
