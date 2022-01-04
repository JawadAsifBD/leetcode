class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res, power = 0, 0
        if n == 0:
            return 1
        while n:
            if not n & 1:
                res += 2**power
            power += 1
            n >>= 1
        return res


s = Solution()
num = 10
print(s.bitwiseComplement(num))
