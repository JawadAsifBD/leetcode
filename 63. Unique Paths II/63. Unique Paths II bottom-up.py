from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for column in range(n):
                if obstacleGrid[row][column] == 1:
                    dp[row][column] = 0
                    continue
                if row > 0:
                    dp[row][column] += dp[row-1][column]
                if column > 0:
                    dp[row][column] += dp[row][column-1]
        return dp[m-1][n-1]
