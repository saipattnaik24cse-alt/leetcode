class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = max(candies)

        while left < right:
            mid = (left + right + 1) // 2
            children = sum(candy // mid for candy in candies)

            if children >= k:
                left = mid
            else:
                right = mid - 1

        return left