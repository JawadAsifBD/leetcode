import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        new_list = sorted(s, key=lambda x: (counts[x], x), reverse=True)
        return ''.join(new_list)


a = Solution()
s = "loveleetcode"
print(a.frequencySort(s))
