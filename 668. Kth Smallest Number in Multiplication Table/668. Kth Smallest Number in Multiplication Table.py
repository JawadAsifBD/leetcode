class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo


m = 9895
n = 28405
k = 100787757
s = Solution()
print(s.findKthNumber(m, n, k))
