class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s:
            count1[ord(ch) - ord('a')] += 1

        for ch in t:
            count2[ord(ch) - ord('a')] += 1

        return count1 == count2