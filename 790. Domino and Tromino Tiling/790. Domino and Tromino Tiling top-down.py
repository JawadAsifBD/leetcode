from functools import lru_cache


class Solution:
    def numTilings(self, n: int) -> int:
        modulo = 10**9+7

        @lru_cache(None)
        def dp(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i == 3:
                return 5
            return (dp(i-1)*2 + dp(i-3)) % modulo
        return dp(n)


s = Solution()
n = 6
print(s.numTilings(n))
