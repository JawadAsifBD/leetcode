class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i: int, j: int) -> int:
            if i == m:
                return 0
            if j == n:
                return 0
            if memo[i][j] == -1:
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + dp(i+1, j+1)
                else:
                    memo[i][j] = max(dp(i+1, j), dp(i, j+1))
            return memo[i][j]

        m = len(text1)
        n = len(text2)
        memo = [[-1]*n for _ in range(m)]
        return dp(0, 0)


s = Solution()
text1 = "abcde"
text2 = "ace"
print(s.longestCommonSubsequence(text1, text2))
