class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res.reverse()
        r = " "
        return r.join(res)


s = "  hello world  "
a = Solution()
print(a.reverseWords(s))
