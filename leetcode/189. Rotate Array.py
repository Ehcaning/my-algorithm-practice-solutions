def rotate_1(nums, k):
    left, right = nums[:-k], nums[-k:]
    nums = left[::-1]+right[::-1]
    nums = nums[::-1]

    return nums


def rotate_2(nums, k):
    k = k % len(nums)
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    print(','.join(str(x) for x in nums))
    left = 0
    right = k-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    print(','.join(str(x) for x in nums))
    left = k
    right = len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


print(
    rotate_1([1, 2, 3, 4, 5, 6, 7], 3),
)
print("------------------------")
print(
    rotate_2([1, 2, 3, 4, 5, 6, 7], 3),
)

"""
k: 3
0 1 2 3 4 5 6 7 8    index

1 2 3 4 5 6 7 8 9
4 2 3 4 5 6 7 8 9


"""
