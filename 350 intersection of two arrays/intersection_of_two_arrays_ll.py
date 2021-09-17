from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            larger_of_two_list = nums1
            smaller_of_two_list = nums2
        else:
            larger_of_two_list = nums2
            smaller_of_two_list = nums1

        result = []
        for i in smaller_of_two_list:
            if i in larger_of_two_list:
                result.append(i)
                larger_of_two_list.remove(i)
        return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
s = Solution()
print(s.intersect(nums1=nums1, nums2=nums2))
