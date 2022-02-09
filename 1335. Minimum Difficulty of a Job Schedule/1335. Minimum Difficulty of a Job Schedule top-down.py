from math import floor
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        n = len(jobDifficulty)
        memo = [[-1]*(d+1) for _ in range(n)]

        def dp(i: int, day: int) -> int:
            # check memo
            if memo[i][day] == -1:
                # base case
                if day == 1:
                    memo[i][day] = max([jobDifficulty[j] for j in range(i, n)])
                else:
                    # maximum possible difficulty of a day 300*1000
                    min_for_day = 300001
                    for j in range(1, n-i):
                        min_for_day = min(min_for_day, max(
                            jobDifficulty[i:i+j])+dp(i+j, day-1))
                    memo[i][day] = min_for_day
            return memo[i][day]

        return dp(0, d)


# jobDifficulty = [6, 5, 4, 3, 2, 1]
# d = 2
jobDifficulty = [9, 9, 9]
d = 4
# jobDifficulty = [1, 1, 1]
# d = 3
s = Solution()
print(s.minDifficulty(jobDifficulty, d))
