from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n

        # sort by start and end point
        START, END = 0, 1
        points.sort(key=lambda i: (i[START], i[END]))
        prev, cur = points[0], None
        darts = 0

        for i in range(1, n):
            cur = points[i]

            if cur[START] <= prev[END]:
                # overlap, wait for more overlap to throw dart
                prev = [cur[START], min(cur[END], prev[END])]
            else:
                # no overlap, throw dart at previous
                darts += 1
                prev = cur

        return darts+1


s = Solution()
# points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# points = [[1, 2], [3, 4], [5, 6], [7, 8]]
points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
print(s.findMinArrowShots(points))
