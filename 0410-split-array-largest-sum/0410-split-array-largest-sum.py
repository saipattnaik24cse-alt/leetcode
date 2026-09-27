class Solution:
    def splitArray(self, nums, k):

        left = max(nums)
        right = sum(nums)

        while left <= right:

            max_sum = (left + right) // 2

            current_sum = 0
            subarrays = 1

            for num in nums:

                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = 0

                current_sum += num

            if subarrays <= k:
                right = max_sum - 1
            else:
                left = max_sum + 1

        return left