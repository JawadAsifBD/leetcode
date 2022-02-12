from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(s: str):
            if s in wordDict:
                return True
            for i in range(1, len(s)):
                if dp(s[:i]) and dp(s[i:]):
                    return True
            return False

        return dp(s)


a = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(a.wordBreak(s, wordDict))
