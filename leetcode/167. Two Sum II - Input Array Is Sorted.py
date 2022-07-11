def twoSum(nums, target):
    store = {}
    for i, val in enumerate(nums):
        remaining = target - nums[i]

        if remaining in store:
            return [store[remaining]+1, i+1]

        store[val] = i
    return []


assert twoSum([2, 7, 11, 15], 9) == [1, 2]
assert twoSum([2, 3, 4], 6) == [1, 3]
assert twoSum([-1, 0], -1) == [1, 2]
