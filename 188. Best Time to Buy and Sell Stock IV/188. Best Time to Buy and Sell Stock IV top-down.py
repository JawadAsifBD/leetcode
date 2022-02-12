from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, trxn_remaining: int, holding: bool) -> int:
            # base case
            if i == len(prices) or trxn_remaining == 0:
                return 0

            do_nothing = dp(i+1, trxn_remaining, holding)
            do_something = 0

            if holding:
                # sell
                do_something = prices[i] + dp(i+1, trxn_remaining-1, False)
            else:
                # buy
                do_something = -prices[i] + dp(i+1, trxn_remaining, True)
            return max(do_nothing, do_something)

        return dp(0, k, False)
