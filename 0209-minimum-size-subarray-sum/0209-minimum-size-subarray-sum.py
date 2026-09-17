class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        k = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                k = min(k, right - left + 1)

                window_sum -= nums[left]
                left += 1

        if k == float('inf'):
            return 0

        return k