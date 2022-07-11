def maxSubArray(nums):
    current_largest_sum = left = nums[0]
    for i in range(1, len(nums)):
        right = max(left + nums[i], nums[i])
        if right > current_largest_sum:
            current_largest_sum = right
        left = right
    return current_largest_sum


print(
    maxSubArray(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    )
)
