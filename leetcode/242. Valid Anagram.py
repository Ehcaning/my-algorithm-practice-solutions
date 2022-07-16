def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_map = {}
    for char in s:
        count_map[char] = count_map.get(char, 0) + 1

    for char in t:
        if char not in count_map:
            return False
        if count_map[char] <= 0:
            return False
        count_map[char] -= 1

    return True


assert isAnagram("anagram", "nagaram") is True
assert isAnagram("rat", "car") is False
