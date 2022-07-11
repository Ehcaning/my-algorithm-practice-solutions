def sortedSquares(nums):
    left = 0
    right = len(nums)-1
    pointer = len(nums)-1
    ans = [None] * len(nums)

    while(right >= left):
        if abs(nums[right]) <= abs(nums[left]):
            ans[pointer] = nums[left]**2
            left += 1
        else:
            ans[pointer] = nums[right]**2
            right -= 1
        pointer -= 1

    return ans


print(
    sortedSquares([-4, -1, 0, 3, 10])
)
