from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(None)
        def dp(row: int, column: int) -> int:
            if obstacleGrid[row][column] == 1:
                return 0
            if row+column == 0:
                return 1
            ways = 0
            if row > 0:
                ways += dp(row-1, column)
            if column > 0:
                ways += dp(row, column-1)
            return ways
        return dp(m-1, n-1)
