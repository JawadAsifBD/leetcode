class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        temp_result = 0
        for i in nums:
            if i == 1:
                temp_result = temp_result + 1
            else:
                if temp_result > result:
                    result = temp_result
                temp_result = 0

        if temp_result > result:
            result = temp_result
        return result
