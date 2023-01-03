from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            last_char = 0
            for str in strs:
                if ord(str[i]) < last_char:
                    count += 1
                    break
                else:
                    last_char = ord(str[i])
        return count


s = Solution()
strs = ["zyx", "wvu", "tsr"]
print(s.minDeletionSize(strs=strs))
