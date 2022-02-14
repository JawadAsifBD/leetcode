class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        prev = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            cur = [0, 0, 0, 0, 0]
            for ch in range(5):
                if ch == 0:
                    # prev ends with a will end with e
                    cur[1] += prev[ch]
                elif ch == 1:
                    # prev ends with e will end with a or i
                    cur[0] += prev[ch]
                    cur[2] += prev[ch]
                elif ch == 2:
                    # prev ends with i will end with a, e, o, u
                    cur[0] += prev[ch]
                    cur[1] += prev[ch]
                    cur[3] += prev[ch]
                    cur[4] += prev[ch]
                elif ch == 3:
                    # prev ends with o will end with u or i
                    cur[2] += prev[ch]
                    cur[4] += prev[ch]
                else:
                    cur[0] += prev[ch]
            prev = cur
        return sum(prev) % (10 ** 9 + 7)
