from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        x = (10 ** 9 + 7)

        @lru_cache(None)
        def dp(char_left: int, vowel: chr) -> int:
            # condition according to problem statement
            if vowel == 'a':
                # Each vowel 'a' may only be followed by an 'e'.
                if char_left == 1:
                    return 1
                return dp(char_left-1, 'e') % x
            elif vowel == 'e':
                # Each vowel 'e' may only be followed by an 'a' or an 'i'.
                if char_left == 1:
                    return 2
                return dp(char_left-1, 'a') + dp(char_left-1, 'i') % x
            elif vowel == 'i':
                # Each vowel 'i' may not be followed by another 'i'.
                if char_left == 1:
                    return 4
                res = 0
                for i in vowels:
                    if i != 'i':
                        res += dp(char_left-1, i)
                return res % x
            elif vowel == 'o':
                # Each vowel 'o' may only be followed by an 'i' or a 'u'.
                if char_left == 1:
                    return 2
                return dp(char_left-1, 'i') + dp(char_left-1, 'u') % x
            elif vowel == 'u':
                # Each vowel 'u' may only be followed by an 'a'.
                if char_left == 1:
                    return 1
                return dp(char_left-1, 'a') % x
            else:
                # vowel = None
                if char_left == 1:
                    return 5
                return sum(dp(char_left-1, i) for i in vowels) % x

        return dp(n, None)
