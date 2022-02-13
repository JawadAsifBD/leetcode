from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dp(row: int, column: int) -> int:
            ways = grid[row][column]
            if row > 0 and column > 0:
                ways += min(dp(row-1, column), dp(row, column-1))
            elif row > 0:
                ways += dp(row-1, column)
            elif column > 0:
                ways += dp(row, column-1)
            return ways
        return dp(m-1, n-1)
