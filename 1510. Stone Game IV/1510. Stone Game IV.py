from functools import lru_cache
from math import floor, sqrt


class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if not n:
            return False

        for i in reversed(range(1, floor(sqrt(n)) + 1)):
            if not self.winnerSquareGame(n - i**2):
                return True

        return False


s = Solution()
n = 400
print(s.winnerSquareGame(n))
