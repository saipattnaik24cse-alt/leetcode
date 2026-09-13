class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

            if hashmap[num] > len(nums) // 2:
                return num