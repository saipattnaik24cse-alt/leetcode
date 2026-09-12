class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap = {}


        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i

        return -1
        