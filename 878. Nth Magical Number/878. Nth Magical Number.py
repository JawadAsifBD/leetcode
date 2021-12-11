class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7

        a, b = min(a, b), max(a, b)
        lcm = a * b / self.gcd(a, b)  # least common multiple

        lo, hi = a, b * 10**9  # from the constraint
        while lo <= hi:
            mid = (lo + hi) // 2

            curN = mid // a + mid // b - mid // lcm
            if curN == n:
                res = mid - min(mid % a, mid % b)
                return res % mod

            if curN < n:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def gcd(self, a, b):  # greatest common divisor
        while b > 0:
            temp, b = b, a % b
            a = temp

        return a
