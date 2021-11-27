class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prev = 1
        for i in range(n):
            result[i] *= prev
            prev *= nums[i]
        prev = 1
        for i in range(n-1, -1, -1):
            result[i] *= prev
            prev *= nums[i]
        return result
