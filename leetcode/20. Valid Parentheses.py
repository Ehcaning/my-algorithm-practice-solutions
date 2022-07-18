class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = {"[", "{", "("}
        close_chars = {"]", "}", ")"}

        stack = []
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif char in close_chars:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if not self.is_same_type(poped, char):
                    return False
            else:
                return False
        return len(stack) == 0

    def is_same_type(self, ch1, ch2):
        return (ch1 == "[" and ch2 == "]") or (ch1 == "{" and ch2 == "}") or (ch1 == "(" and ch2 == ")")


s = Solution()
assert s.isValid("()") is True
assert s.isValid("()[]{}") is True
assert s.isValid("(]") is False
assert s.isValid("({[]})") is True
assert s.isValid("][") is False
