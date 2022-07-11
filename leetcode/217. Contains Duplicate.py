
def containsDuplicate(nums):
    to_find = {}
    for n in nums:
        if n in to_find:
            return False
        else:
            to_find[n] = True

    return True


print(
    containsDuplicate([1, 2, 3, 1])
)
