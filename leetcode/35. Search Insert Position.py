def searchInsert(nums, target):
    if len(nums) == 1:
        if nums[0] >= target:
            return 0
        else:
            return 1
    left, right = 0, len(nums)-1
    while(left < right):
        if right - left == 1:
            if nums[right] == target:
                return right
            elif nums[left] >= target:
                return left
            elif nums[right] < target:
                return right+1
            else:
                return left+1
        pivot = left + (right-left) // 2
        if nums[pivot] == target:
            return pivot
        if nums[pivot] > target:
            right = pivot
            continue
        else:
            left = pivot
            continue
    return left+1
