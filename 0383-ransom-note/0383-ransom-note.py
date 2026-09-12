class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in magazine:
            count1[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            count2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if count2[i] > count1[i]:
                return False

        return True