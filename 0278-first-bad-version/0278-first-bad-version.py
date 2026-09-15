# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans