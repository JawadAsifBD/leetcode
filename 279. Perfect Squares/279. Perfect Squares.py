import math
from typing import List
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        res = 0
        squareList = []
        r = int(math.sqrt(n))
        for num in range(1, r+1):
            squareList.append(num ** 2)
        dp = [sys.maxsize for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            for j in range(r):
                if i < squareList[j]:
                    break
                dp[i] = min(dp[i], dp[i-squareList[j]]+1)
        return dp[n]


s = Solution()
n = 44
print(s.numSquares(n))
