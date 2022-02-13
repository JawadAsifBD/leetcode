from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(row: int, column: int) -> int:
            if row+column == 0:
                return 1
            ways = 0
            if row > 0:
                ways += dp(row-1, column)
            if column > 0:
                ways += dp(row, column-1)
            return ways
        return dp(m-1, n-1)
