from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        res = 0
        for i in range(len(cost)):
            if i % 3 == 0:
                res += cost[i]
            elif i % 3 == 1:
                res += cost[i]
        return res


s = Solution()
cost = [6, 5, 7, 9, 2, 2]
print(s.minimumCost(cost))
