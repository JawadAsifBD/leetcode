class Solution:

    def findMin(self, nums: List[int]) -> int:

        val = sys.maxsize

        for i in nums:

            if i < val:

                val = i

        return val
