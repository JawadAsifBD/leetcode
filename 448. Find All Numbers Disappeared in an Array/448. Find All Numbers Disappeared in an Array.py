from typing import Counter


class Solution:
    def findDisappearedNumbers(self, nums):
        s = Counter(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]


s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums))
