class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > maxArea:
                maxArea = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea