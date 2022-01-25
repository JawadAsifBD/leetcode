from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        is_decreasing = False
        is_increasing = False

        # length less than 3
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            # found downward slope, but element is larger than previous
            if is_decreasing and arr[i] > arr[i-1]:
                return False

            # elements are equal
            if arr[i] == arr[i-1]:
                return False
            # detect downward slope
            elif arr[i] < arr[i-1]:
                is_decreasing = True
            # detect upward slope
            elif arr[i] > arr[i-1]:
                is_increasing = True
        # a mountain array must have a peak and downard slope,
        # but in this case, array is strictly increasing or strictly decreasing
        if not is_decreasing or not is_increasing:
            return False
        return True


s = Solution()
# arr = [3, 5, 5]
# arr = [0, 3, 2, 1]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(s.validMountainArray(arr))
