from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        mods = [0 for _ in range(60)]
        for i in time:
            mods[i % 60] += 1
        for i in range(1, 30):
            res += mods[i]*mods[60-i]
        res += mods[0]*(mods[0]-1)//2
        res += mods[30]*(mods[30]-1)//2
        return res


s = Solution()
time = [30, 20, 150, 100, 40]
print(s.numPairsDivisibleBy60(time))
