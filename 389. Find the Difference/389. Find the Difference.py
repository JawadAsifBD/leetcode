class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(t)):
            if i == len(s) or t[i] != s[i]:
                return t[i]


s = "abcd"
t = "abcde"
a = Solution()
print(a.findTheDifference(s, t))
