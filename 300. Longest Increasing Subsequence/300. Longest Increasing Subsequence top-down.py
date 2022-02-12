from functools import lru_cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            # base case
            if i == 0:
                return 1
            # recurrence relation
            res = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, 1+dp(j))
            return res

        return max(dp(i) for i in range(len(nums)))
