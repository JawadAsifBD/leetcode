# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        start = 1
        end = n
        res = start + (end-start)//2
        g = guess(res)
        while g != 0:
            if g > 0:
                start = res + 1
            else:
                end = res - 1
            res = start + (end-start)//2
            g = guess(res)

        return res


def guess(n: int) -> int:
    num = 4
    if n == num:
        return 0
    elif n < num:
        return 1
    else:
        return -1


s = Solution()
n = 5
print(s.guessNumber(n))
