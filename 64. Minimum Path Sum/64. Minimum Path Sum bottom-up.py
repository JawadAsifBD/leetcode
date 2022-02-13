from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        for row in range(m):
            for column in range(n):
                dp[row][column] += grid[row][column]
                if row > 0 and column > 0:
                    dp[row][column] += min(dp[row-1]
                                           [column], dp[row][column-1])
                elif row > 0:
                    dp[row][column] += dp[row-1][column]
                elif column > 0:
                    dp[row][column] += dp[row][column-1]
        return dp[m-1][n-1]
