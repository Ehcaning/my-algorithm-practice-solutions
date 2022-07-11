def firstBadVersion(n):
    left, right = 1, n
    while(left < right):
        if right - left <= 1:
            if isBadVersion(left) is True:
                return left
            else:
                return right

        pivot = left + (right-left)//2
        if isBadVersion(pivot) is True:
            right = pivot
            continue
        else:
            left = pivot
            continue
    return left


def isBadVersion(version):
    pass
