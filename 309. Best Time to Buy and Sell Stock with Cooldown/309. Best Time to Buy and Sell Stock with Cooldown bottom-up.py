from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for holding in range(2):
                do_nothing = dp[i+1][holding]
                if holding:
                    # sell stock
                    do_something = prices[i] + \
                        dp[i+2][0] if i < n-1 else prices[i]
                else:
                    # buy stock
                    do_something = -prices[i] + dp[i+1][1]
                dp[i][holding] = max(do_nothing, do_something)
        return dp[0][0]
