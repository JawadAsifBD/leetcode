from typing import Counter, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 2
        while True:
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.pop(i)
                i -= 1
            if i == len(nums)-1:
                break
            i += 1
        return len(nums)


s = Solution()
nums = [1, 1, 1, 2, 2, 3]
print(s.removeDuplicates(nums))
