from math import ceil
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, dist = 0, seats.index(1)

        for seat in seats:
            if seat:
                res, dist = max(res, ceil(dist/2)), 0
            else:
                dist += 1

        return max(res, dist)


s = Solution()
# seats = [1, 0, 0, 0, 1, 0, 1]
# seats = [1, 0, 0, 0]
# seats = [0, 1]
# seats = [1, 0, 0, 1]
seats = [0, 1, 0, 1, 0]
print(s.maxDistToClosest(seats))
