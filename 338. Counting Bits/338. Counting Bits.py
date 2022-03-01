from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                count += i & 1
                i = i >> 1
            res.append(count)
        return res


s = Solution()
n = 5
print(s.countBits(n))
