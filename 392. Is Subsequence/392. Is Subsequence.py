from functools import lru_cache
from operator import truediv


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])


a = Solution()
s = "axc"
t = "ahbgdc"
print(a.isSubsequence(s, t))
