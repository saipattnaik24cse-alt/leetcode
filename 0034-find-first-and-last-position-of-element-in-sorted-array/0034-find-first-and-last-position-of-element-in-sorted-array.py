class Solution:
    def searchRange(self, nums, target):

        def find_first():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        def find_last():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [find_first(), find_last()]