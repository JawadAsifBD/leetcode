from functools import lru_cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @lru_cache(None)
        def dp(row: int, column: int) -> int:
            ways = matrix[row][column]
            if row == 0:
                return ways
            if column > 0 and column < n-1:
                ways += min(
                    dp(row-1, column-1), dp(row-1, column), dp(row-1, column+1))
            elif column > 0:
                ways += min(
                    dp(row-1, column-1), dp(row-1, column))
            elif column < n-1:
                ways += min(
                    dp(row-1, column), dp(row-1, column+1))
            return ways

        return min(dp(m-1, i) for i in range(n))
