def canConstruct(ransomNote, magazine):
    magMap = {}
    for letter in magazine:
        if letter in magMap:
            magMap[letter] += 1
        else:
            magMap[letter] = 1
    for letter in ransomNote:
        if letter not in magMap:
            return False
        if magMap[letter] == 0:
            return False
        magMap[letter] -= 1
    return True


assert canConstruct("a", "b") is False
assert canConstruct("aa", "ab") is False
assert canConstruct("aa", "aab") is True
