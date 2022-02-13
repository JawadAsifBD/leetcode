from functools import lru_cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def dp(amount: int, coin_index: int) -> int:
            # base case
            if coin_index >= n or amount < 0:
                return 0
            if amount == 0:
                return 1

            # recurrence relation
            take = dp(amount-coins[coin_index], coin_index)
            notake = dp(amount, coin_index+1)

            return take + notake

        return dp(amount, 0)


s = Solution()
amount = 5
coins = [1, 2, 5]
print(s.change(amount, coins))
