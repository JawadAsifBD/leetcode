class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(0, n):
            if 1 <= int(s[i]) <= 9:
                dp[i+1] += dp[i]
            if i-1 >= 0 and 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[n]


a = Solution()
s = "226"
print(a.numDecodings(s))
