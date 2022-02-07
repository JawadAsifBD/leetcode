class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n not in memo:
                memo[n] = dp(n-1)+dp(n-2) + dp(n-3)
            return memo[n]

        memo = {}
        return dp(n)
