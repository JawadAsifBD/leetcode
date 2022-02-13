from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for row in range(1, m):
            for column in range(n):
                dp[row][column] += matrix[row][column]
                if column > 0 and column < n-1:
                    dp[row][column] += min(
                        dp[row-1][column-1], dp[row-1][column], dp[row-1][column+1])
                elif column > 0:
                    dp[row][column] += min(
                        dp[row-1][column-1], dp[row-1][column])
                elif column < n-1:
                    dp[row][column] += min(
                        dp[row-1][column], dp[row-1][column+1])
        return min(dp[m-1][i] for i in range(n))


s = Solution()
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(s.minFallingPathSum(matrix))
