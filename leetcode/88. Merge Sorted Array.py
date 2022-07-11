def merge(nums1, m, nums2, n):
    end = m+n-1
    end_1 = m - 1
    end_2 = n - 1

    while end_2 >= 0:
        if end_1 >= 0:
            if nums1[end_1] > nums2[end_2]:
                nums1[end] = nums1[end_1]
                end_1 -= 1
            else:
                nums1[end] = nums2[end_2]
                end_2 -= 1
        else:
            nums1[end] = nums2[end_2]
            end_2 -= 1
        end -= 1

    return nums1


assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
assert merge([1], 1, [],  0) == [1]
assert merge([0], 0, [1],  1) == [1]
