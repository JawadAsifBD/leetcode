from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
        return profit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))
