from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, holding: int):
            # base case
            if i >= len(prices):
                return 0

            do_nothing = dp(i+1, holding)
            if holding:
                # sell stock
                do_something = prices[i] + dp(i+2, 0)
            else:
                # buy stock
                do_something = -prices[i] + dp(i+1, 1)

            return max(do_nothing, do_something)
        return dp(0, 0)
