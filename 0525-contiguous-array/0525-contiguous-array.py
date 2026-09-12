class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hashmap = {0: -1}

        count = 0
        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                max_length = max(max_length, i - hashmap[count])
            else:
                hashmap[count] = i

        return max_length