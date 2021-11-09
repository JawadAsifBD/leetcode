from typing import List
from itertools import product


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        res = [0 for _ in range(len(puzzles))]
        for i, j in product(range(len(words)), range(len(puzzles))):
            word = words[i]
            puzzle = puzzles[j]
            flag = 1
            if puzzle[0] not in word:
                flag = 0
            if flag == 1:
                for c in word:
                    if c not in puzzle:
                        flag = 0
                        break
            if flag == 1:
                res[j] += 1
        return res


s = Solution()
# words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
# puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
words = ["apple", "pleas", "please"]
puzzles = ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]
print(s.findNumOfValidWords(words, puzzles))
