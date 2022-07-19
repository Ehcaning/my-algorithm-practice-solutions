class Solution:
    def letterCasePermutation(self, s):
        if len(s) == 1:
            if s.isalpha():
                return [s.lower(), s.upper()]
            else:
                return [s]

        next_results = self.letterCasePermutation(s[1:])

        res = []
        first_char = s[0]
        for next_result in next_results:
            if first_char.isalpha():
                res += [
                    f'{first_char.lower()}{next_result}',
                    f'{first_char.upper()}{next_result}',
                ]
            else:
                res += [
                    f'{first_char}{next_result}'
                ]
        return res


s = Solution()
print(
    s.letterCasePermutation("a1b2")
)
