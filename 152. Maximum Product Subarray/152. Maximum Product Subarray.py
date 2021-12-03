from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod, res = 1, float('-inf')

        for num in nums:
            prod *= num
            res = max(prod, res)

            if prod == 0:
                prod = 1

        prod = 1

        for i in reversed(range(len(nums))):
            prod *= nums[i]
            res = max(prod, res)

            if prod == 0:
                prod = 1

        return res


s = Solution()
nums = [-2, 0, -1]
print(s.maxProduct(nums))
