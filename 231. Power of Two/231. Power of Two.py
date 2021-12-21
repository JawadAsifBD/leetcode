class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not(n & (n-1)) and bool(n)


s = Solution()
n = 0
print(s.isPowerOfTwo(n))
