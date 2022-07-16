class Solution:
    def searchMatrix(self, matrix, target):
        rows, columns = len(matrix), len(matrix[0])

        if matrix[0][0] > target or matrix[rows-1][columns-1] < target:
            return False

        possible_row = self.get_possible_target_row(
            matrix, target, rows, columns)
        if possible_row == -1:
            return False

        for i in range(columns):
            if matrix[possible_row][i] == target:
                return True

        return False

    def get_possible_target_row(self, matrix, target, rows, columns):
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][columns-1] >= target:
                return i
        return -1


s = Solution()
assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                       [23, 30, 34, 60]], 3) is True
assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                       [23, 30, 34, 60]], 13) is False
