class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Frequency of s1
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add new character
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # If window becomes too large
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # Check permutation
            if window_count == s1_count:
                return True

        return False