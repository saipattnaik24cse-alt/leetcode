class Solution:
    def maximumSubarraySum(self, nums, k):
        prefix = 0
        hashmap = {}
        ans = float('-inf')

        for j in range(len(nums)):
            x = nums[j]

            if x - k in hashmap:
                ans = max(ans, prefix + x - hashmap[x - k])

            if x + k in hashmap:
                ans = max(ans, prefix + x - hashmap[x + k])

            prefix += x

            if x not in hashmap:
                hashmap[x] = prefix - x
            else:
                hashmap[x] = min(hashmap[x], prefix - x)

        return int(ans) if ans != float('-inf') else 0