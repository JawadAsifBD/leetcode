from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        new_list = sorted(events, key=lambda x: x[1])
        new_list = sorted(new_list, key=lambda x: (x[2], x[:1]))
        print(new_list)
        return 0


events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
s = Solution()
s.maxTwoEvents(events)
