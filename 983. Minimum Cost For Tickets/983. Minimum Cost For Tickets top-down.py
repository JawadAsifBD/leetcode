from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def dp(day: int) -> int:
            if day > days[-1]:
                return 0
            if day == days[-1]:
                return min(costs)
            else:
                i = 0
                while i < len(days) and days[i] < day:
                    i += 1
                if i == len(days):
                    return 0
                day = days[i]
            return min(costs[0]+dp(day+1), costs[1]+dp(day+7), costs[2]+dp(day+30))
        return dp(days[0])


s = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(s.mincostTickets(days, costs))
