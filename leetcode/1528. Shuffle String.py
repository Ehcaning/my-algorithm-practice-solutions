class Solution:
    def restoreString(self, s, indices):
        res = [""]*len(s)
        for ch, index in zip(s, indices):
            res[index] = ch
        return "".join(res)


s = Solution()
print(
    s.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]),
    "leetcode"
)
print("---")
print(
    s.restoreString("abc", [0, 1, 2]),
    "abc"
)
