class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum == target:
                return [left + 1, right + 1]

            elif currentSum < target:
                left += 1

            else:
                right -= 1