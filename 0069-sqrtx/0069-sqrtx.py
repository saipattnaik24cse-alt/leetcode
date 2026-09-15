class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans