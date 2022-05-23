from functools import lru_cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        def dp(m: int, n: int, idx: int) -> int:
            # base case
            if m < 0 or n < 0:
                return float('-inf')
            if idx == len(strs):
                return 0

            # recurrence relation
            take = 1 + dp(m-counter[idx][0], n-counter[idx][1], idx+1)
            notake = dp(m, n, idx+1)
            return max(take, notake)

        return dp(m, n, 0)


s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
# strs = ["10", "0", "1"]
# m = 1
# n = 1
print(s.findMaxForm(strs=strs, m=m, n=n))
