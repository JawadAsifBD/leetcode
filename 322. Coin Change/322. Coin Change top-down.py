from cgitb import reset
from enum import Flag
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            # base case
            if i == 0:
                return 0
            if i < 0:
                return -1

            # recurrence
            minimum = float('inf')
            for coin in coins:
                res = dp(i-coin)
                if res >= 0 and res < minimum:
                    minimum = 1 + res
            if minimum == float('inf'):
                return -1
            return minimum
        return dp(amount)


s = Solution()
# coins = [1, 2, 5]
# amount = 11
# coins = [3]
# amount = 4
coins = [1, 2147483647]
amount = 2
print(s.coinChange(coins, amount))
