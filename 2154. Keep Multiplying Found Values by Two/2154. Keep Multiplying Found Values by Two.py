from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        m = max(nums)
        while original <= m:
            if original in nums:
                original *= 2
            else:
                break
        return original


s = Solution()
# nums = [5, 3, 6, 1, 12]
# original = 3
nums = [2, 7, 9]
original = 4
print(s.findFinalValue(nums, original))
