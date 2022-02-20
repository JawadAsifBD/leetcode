from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], ~x[1]))
        count = 1
        start, end = intervals[0]
        for i, j in intervals[1:]:
            if i >= start and j <= end:
                continue
            count += 1
            start, end = i, j
        return count


s = Solution()
a = [[1, 2], [1, 4], [3, 4]]
print(s.removeCoveredIntervals(a))
