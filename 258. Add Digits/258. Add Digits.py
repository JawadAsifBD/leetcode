class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while True:
            while num > 0:
                res += num % 10
                num //= 10
            if res < 10:
                return res
            else:
                num = res
                res = 0


s = Solution()
num = 0
print(s.addDigits(num))
