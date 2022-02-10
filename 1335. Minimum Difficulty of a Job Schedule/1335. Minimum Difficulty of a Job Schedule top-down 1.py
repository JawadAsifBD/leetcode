from functools import lru_cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        hardest_job_remaining = [0]*n
        hardest_job = 0

        for i in range(n-1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        @lru_cache(None)
        def dp(i: int, day: int) -> int:
            # base case
            if d == day:
                return hardest_job_remaining[i]

            # recurrence relation
            best = float('inf')
            hardest = 0

            for j in range(i, n-(d-day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j+1, day+1))
            return best
        return dp(0, 1)


# jobDifficulty = [6, 5, 4, 3, 2, 1]
# d = 2
jobDifficulty = [9, 9, 9]
d = 4
# jobDifficulty = [1, 1, 1]
# d = 3
s = Solution()
print(s.minDifficulty(jobDifficulty, d))
