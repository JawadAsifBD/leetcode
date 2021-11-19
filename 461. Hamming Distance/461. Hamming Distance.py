class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        return bin(xor).count('1')


s = Solution()
x = 4
y = 1
print(s.hammingDistance(x, y))
