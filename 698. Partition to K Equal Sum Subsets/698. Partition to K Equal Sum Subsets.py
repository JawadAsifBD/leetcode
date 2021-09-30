from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        sum_per_subset = sum(nums)/k
        nums.sort()
        visited = [False for i in range(len(nums))]
        if sum_per_subset < nums[-1]:
            return False
        return self.dfs(nums, k, sum_per_subset, 0, 0, visited)

    def dfs(self, nums: List[int], k: int, target: int, current_sum: int, start: int, visited: List[bool]) -> bool:
        if k == 1:
            return True
        if current_sum > target:
            return False
        if current_sum == target:
            return self.dfs(nums, k-1, target, 0, 0, visited)
        if start >= len(nums):
            return False
        for i in range(start, len(nums)):
            if visited[i] == True:
                continue
            visited[i] = True
            if self.dfs(nums, k, target, current_sum+nums[i], i+1, visited):
                return True
            visited[i] = False
        return False


s = Solution()
# nums = [3522, 181, 521, 515, 304, 123, 2512, 312,
#         922, 407, 146, 1932, 4037, 2646, 3871, 269]
# k = 5
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
res = s.canPartitionKSubsets(nums, k)
print(res)
