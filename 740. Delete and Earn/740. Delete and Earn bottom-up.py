from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        prev = -1
        avoid = using = 0
        for i in sorted(nums_counter):
            if i - 1 != prev:
                avoid, using = max(avoid, using), i * \
                    nums_counter[i] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), i*nums_counter[i]+avoid
            prev = i
        return max(avoid, using)
