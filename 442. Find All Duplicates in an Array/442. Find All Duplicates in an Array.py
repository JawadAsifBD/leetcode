from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for num in nums:
            if num not in dic.keys():
                dic[num] = 0
            dic[num] = dic[num] + 1
            if dic[num] == 2:
                res.append(num)
        return res


s = Solution()
nums = [1]
print(s.findDuplicates(nums))
