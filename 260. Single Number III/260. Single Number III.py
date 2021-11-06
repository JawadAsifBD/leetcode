class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res =[]
        for i in nums:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
                
        return res
