from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count("0"), s.count("1")] for s in strs]
        dp = [[0] * (n+1) for _ in range(m+1)]

        for zeros, ones in counter:
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
        return dp[m][n]


s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
# strs = ["10", "0", "1"]
# m = 1
# n = 1
print(s.findMaxForm(strs=strs, m=m, n=n))
