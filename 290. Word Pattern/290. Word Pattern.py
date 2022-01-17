class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        words, w_to_p = s.split(' '), dict()

        if len(p) != len(words):
            return False
        if len(set(p)) != len(set(words)):
            return False  # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = p[i]
            elif w_to_p[words[i]] != p[i]:
                return False

        return True


sol = Solution()
# pattern = "aaaa"
# s = "dog cat cat dog"
# pattern, s = "abba", "dog cat cat dog"
# pattern, s = "abba", "dog cat cat fish"
# pattern, s = "aaaa", "dog cat cat dog"
# pattern, s = "aaaa", "dog dog dog dog"
pattern, s = "abba", "dog dog dog dog"
print(sol.wordPattern(pattern, s))
