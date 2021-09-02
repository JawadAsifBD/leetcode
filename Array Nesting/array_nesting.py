class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        visited = [False]*len(nums)
        for index,_ in enumerate(nums):
            if visited[index] is False:
                count = 0
                i = index
                while visited[i] is False:
                    count = count + 1
                    visited[i] = True
                    i = nums[i]
                res = max(res,count)
        return res
