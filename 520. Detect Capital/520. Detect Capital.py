class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper() or word.istitle():
            return True
        return False


s = Solution()
word = 'leetcode'
print(s.detectCapitalUse(word))
