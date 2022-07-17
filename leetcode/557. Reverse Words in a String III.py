
class Solution:
    def reverseWords(self, s):
        ss = s.split()
        ss = [c[::-1] for c in ss]
        return ' '.join(ss)


s = Solution()

assert s.reverseWords(
    "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert s.reverseWords("God Ding") == "doG gniD"
