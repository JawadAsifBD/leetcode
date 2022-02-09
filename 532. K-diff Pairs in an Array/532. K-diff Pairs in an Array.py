from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = i = 0
        j = i+1
        memo = []
        while i < len(nums):
            if j < len(nums) and nums[j]-nums[i] == k and (nums[j], nums[i]) not in memo:
                res += 1
                memo.append((nums[j], nums[i]))
            if j >= len(nums) or nums[j]-nums[i] > k:
                i += 1
                j = i
            j += 1
        return res


s = Solution()
# nums = [3, 1, 4, 1, 5]
# k = 2
# nums = [-1, -2, -3]
# k = 1
nums = [1, 2, 3, 4, 5]
k = 0
print(s.findPairs(nums, k))
