from functools import lru_cache
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def getComb(i: int, target: int, comb: List[int]) -> None:
            if target == 0:
                res.append(comb)
                return
            if i == n:
                return
            for j in range(i, n):
                if candidates[j] <= target:
                    a = comb[:]
                    a.append(candidates[j])
                    getComb(j, target-candidates[j], a)

        getComb(0, target, [])
        return res


s = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum(candidates, target))
