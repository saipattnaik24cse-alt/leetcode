class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1

        while left < right:
            value = nums[left] + nums[right]

            if value == target:
                return [left + 1, right + 1]

            elif value < target:
                left += 1

            else:
                right -= 1