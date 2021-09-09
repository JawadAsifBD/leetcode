from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = [i % 26 for i in shifts]
        # print(shifts)
        finalshifts = [sum(shifts[i:]) % 26 for i in range(len(shifts))]
        # print(finalshifts)

        res = ''
        for i in range(0, len(finalshifts)):
            # print((ord(s[i])+finalshifts[i]) % 26)
            res += chr((ord(s[i])+finalshifts[i]-ord('a')) % 26+ord('a'))

        # print(res)
        return res


s = Solution()
str1 = "mkgfzkkuxownxvfvxasy"
shifts = [505870226, 437526072, 266740649, 224336793, 532917782, 311122363,
          567754492, 595798950, 81520022, 684110326, 137742843, 275267355, 856903962,
          148291585, 919054234, 467541837, 622939912, 116899933, 983296461, 536563513]

s.shiftingLetters(str1, shifts)
