from typing import List
from itertools import product


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        # print(dp)

        # Initialization value
        dp[m-1][n] = 1
        dp[m][n-1] = 1

        # print(dp)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # print(str(i) + " " + str(j))
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)

        return dp[0][0]


s = Solution()
dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
res = s.calculateMinimumHP(dungeon)
print(res)
