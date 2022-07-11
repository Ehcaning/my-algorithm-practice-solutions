def moveZeroes(nums):
    if len(nums) == 1:
        return nums
    insert_index = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        else:
            nums[insert_index] = nums[i]
            insert_index += 1
    for j in range(insert_index, len(nums)):
        nums[j] = 0
    return nums


print(
    moveZeroes([0, 1, 0, 3, 12])
)
