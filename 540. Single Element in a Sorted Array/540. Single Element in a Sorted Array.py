from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high - low)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]


s = Solution()
nums = [3, 3, 7, 7, 10, 11, 11]
print(s.singleNonDuplicate(nums))
