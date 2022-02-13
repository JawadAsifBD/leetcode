from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        curr = 0
        for i in range(2, len(cost)+1):
            prev, curr = curr, min(cost[i-1]+curr, cost[i-2]+prev)
        return curr
