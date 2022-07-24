def majorityElement(nums):
    d = {}
    majority_num = len(nums) // 2
    for num in nums:
        d[num] = d.get(num, 0) + 1
        if d[num] > majority_num:
            return num
    return None


assert majorityElement([3, 2, 3]) == 3
assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
