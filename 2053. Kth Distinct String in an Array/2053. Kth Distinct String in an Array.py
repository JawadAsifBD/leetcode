from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = {}
        for s in arr:
            if s in res.keys():
                res[s] += 1
            else:
                res[s] = 0
        r = ""
        val = 0
        for s in arr:
            if res[s] == 0:
                r = s
                val += 1
                if val == k:
                    return r
                else:
                    r = ""
        return r


arr = ["d", "b", "c", "b", "c", "a"]
k = 2
s = Solution()
print(s.kthDistinct(arr, k))
