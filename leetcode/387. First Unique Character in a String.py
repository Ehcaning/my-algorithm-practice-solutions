def firstUniqChar(s):
    count_map = {}
    for ch in s:
        count_map[ch] = count_map.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if count_map[ch] == 1:
            return i

    return -1


assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1
