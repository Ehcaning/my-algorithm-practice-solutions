class Solution:
    def intersect(self, nums1, nums2):
        counts_map_1 = self.get_counts_map(nums1)
        counts_map_2 = self.get_counts_map(nums2)

        unique_numbers_1 = list(set(nums1))
        result = []
        for number in unique_numbers_1:
            count_of_intersection = min(
                counts_map_1.get(number, 0), counts_map_2.get(number, 0)
            )
            result = result + [number] * count_of_intersection
        return result

    def get_counts_map(self, arr):
        counts_map = {}
        for i in arr:
            counts_map[i] = counts_map.get(i, 0) + 1
        return counts_map


s = Solution()
assert s.intersect([1, 2, 2, 1],  [2, 2]) == [2, 2]
assert s.intersect([4, 9, 5],  [9, 4, 9, 8, 4]) == [9, 4]
