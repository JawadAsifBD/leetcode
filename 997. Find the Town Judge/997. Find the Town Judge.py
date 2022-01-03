from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to, trusted = defaultdict(int), defaultdict(int)

        for a, b in trust:
            trust_to[a] += 1
            trusted[b] += 1

        for i in range(1, n+1):
            if trust_to[i] == 0 and trusted[i] == n - 1:
                return i

        return -1


s = Solution()
n = 1
# trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
trust = []
print(s.findJudge(n, trust))
