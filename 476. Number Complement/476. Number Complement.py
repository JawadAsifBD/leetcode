class Solution:
    def findComplement(self, num: int) -> int:
        res, n = 0, 0
        while num:
            if not num & 1:
                res += 2**n
            n += 1
            num >>= 1
        return res


s = Solution()
num = 5
print(s.findComplement(num))
