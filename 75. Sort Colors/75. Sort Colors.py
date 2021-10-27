class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1
        x = []
        for i, n in enumerate(count):
            x.extend([i]*n)
        for i in range(len(nums)):
            nums[i] = x[i]
