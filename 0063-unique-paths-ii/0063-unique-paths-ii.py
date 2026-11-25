from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If start or end is blocked, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # dp[j] = number of ways to reach cell (current row, j)
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0              # obstacle: no way to reach this cell
                elif j > 0:
                    dp[j] += dp[j - 1]     # from above (dp[j]) + from left (dp[j-1])

        return dp[n - 1]


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(sol.uniquePathsWithObstacles([[0, 1], [0, 0]]))                    # 1
    print(sol.uniquePathsWithObstacles([[1, 0]]))                            # 0