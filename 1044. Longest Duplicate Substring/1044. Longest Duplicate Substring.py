from typing import DefaultDict


class Solution:
    def longestDupSubstring(self, s: str) -> str:

        # Hint 2: To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.
        def RabinKarp(text, L):
            assert L > 0

            q = (1 << 31) - 1
            h, t, d = (1 << (8*L-8)) % q, 0, 256
            dic = DefaultDict(list)

            for i in range(L):
                t = (d * t + ord(text[i])) % q

            dic[t].append(i-L+1)

            for i in range(len(text) - L):
                t = (d*(t-ord(text[i])*h) + ord(text[i + L])) % q
                for j in dic[t]:
                    if text[i+1:i+L+1] == text[j:j+L]:
                        return text[j:j+L]
                dic[t].append(i+1)
            return None

        rst = ""

        # Hint 1: Binary search for the length of the answer.
        l, h = 1, len(s)-1
        while l <= h:
            m = l + (h-l)//2
            dup = RabinKarp(s, m)

            # print(l,h,m,dup)
            if dup:  # if have a duplicate we ask more, search the upper half without the middle
                l = m+1
                rst = dup
            else:   # search the lower half without the middle
                h = m-1
            # print("--", l,m,h, dup)
        return rst
