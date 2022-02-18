from functools import lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9+7
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for dice_left in range(1, n+1):
            for target_left in range(1, target+1):
                for i in range(1, min(k, target_left)+1):
                    dp[dice_left][target_left] += dp[dice_left-1][target_left-i]
                dp[dice_left][target_left] %= modulo
        return dp[n][target]


n = 30
k = 30
target = 500
s = Solution()
print(s.numRollsToTarget(n, k, target))
