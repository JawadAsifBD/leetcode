from functools import lru_cache
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        maxlen = 0

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            nonlocal maxlen
            if i == m:
                return 0
            if j == n:
                return 0

            dp(i+1, j)
            dp(i, j+1)
            if nums1[i] == nums2[j]:
                res = 1 + dp(i+1, j+1)
                maxlen = max(maxlen, res)
                return res
            else:
                return 0

        dp(0, 0)
        return maxlen


s = Solution()
# nums1 = [1, 2, 3, 2, 1]
# nums2 = [3, 2, 1, 4, 7]
# nums1 = [0, 1, 1, 1, 1]
# nums2 = [1, 0, 1, 0, 1]
nums1 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
print(s.findLength(nums1, nums2))
