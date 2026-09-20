class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        result = []

        if len(p) > len(s):
            return result

        p_count = {}
        window_count = {}

        
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1

        left = 0

        for right in range(len(s)):

            
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            
            if right - left + 1 > len(p):

                remove_char = s[left]
                window_count[remove_char] -= 1

                if window_count[remove_char] == 0:
                    del window_count[remove_char]

                left += 1

          
            if window_count == p_count:
                result.append(left)

        return result