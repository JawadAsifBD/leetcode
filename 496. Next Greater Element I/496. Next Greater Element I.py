from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            val = -1
            for index, j in enumerate(nums2):
                # print(j, index)
                if i == j:
                    for k in nums2[index+1:]:
                        if k > i:
                            val = k
                            break
                    break
            res.append(val)
        return res


s = Solution()
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(s.nextGreaterElement(nums1, nums2))
