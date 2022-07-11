def twoSum(nums, target):
    store = {}
    for i, val in enumerate(nums):
        remaining = target - nums[i]

        if remaining in store:
            return [store[remaining], i]

        store[val] = i
    return []


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
