class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while(i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


s = Solution()
assert s.reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
assert s.reverseString(["H", "a", "n", "n", "a", "h"]) == [
    "h", "a", "n", "n", "a", "H"]
