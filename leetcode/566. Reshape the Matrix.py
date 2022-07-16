class Solution:
    def matrixReshape(self, nums, r, c):
        if nums == [] or r * c != len(nums) * len(nums[0]):
            return nums

        res = [[0 for j in range(c)] for i in range(r)]
        k = 0

        for row in nums:
            for num in row:
                res[k // c][k % c] = num
                k += 1

        return res


s = Solution()

assert s.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
assert s.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
