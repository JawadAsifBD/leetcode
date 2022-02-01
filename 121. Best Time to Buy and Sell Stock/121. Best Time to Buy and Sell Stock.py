from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = max(profit, prices[i]-minimum)
        return profit


s = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(s.maxProfit(prices))
