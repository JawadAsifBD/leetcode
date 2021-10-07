from typing import List
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, j in product(range(len(board)), range(len(board[0]))):
            if board[i][j] == word[0]:
                # found first letter
                if len(word) == 1:
                    # found complete word
                    return True
                else:
                    a, word = word[0], word[1:]
                    temp = board[i][j]
                    board[i][j] = '0'
                    if self.dfs(board, word, i, j):
                        return True
                    board[i][j] = temp
                    word = a+word
        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        if j == 0:
            pass  # no left
        else:
            # left
            k = i
            l = j-1
            left = board[k][l]
            if left == word[0]:  # found first letter
                if len(word) == 1:
                    # found complete word
                    return True
                else:
                    a, word = word[0], word[1:]
                    temp = board[k][l]
                    board[k][l] = '0'
                    if self.dfs(board, word, k, l):
                        return True
                    board[k][l] = temp
                    word = a+word
        if i == 0:
            pass  # no up
        else:
            # up
            k = i-1
            l = j
            up = board[k][l]
            if up == word[0]:  # found first letter
                if len(word) == 1:
                    # found complete word
                    return True
                else:
                    a, word = word[0], word[1:]
                    temp = board[k][l]
                    board[k][l] = '0'
                    if self.dfs(board, word, k, l):
                        return True
                    board[k][l] = temp
                    word = a+word

        if i == len(board)-1:
            pass  # no down
        else:
            # down
            k = i+1
            l = j
            down = board[k][l]
            if down == word[0]:  # found first letter
                if len(word) == 1:
                    # found complete word
                    return True
                else:
                    a, word = word[0], word[1:]
                    temp = board[k][l]
                    board[k][l] = '0'
                    if self.dfs(board, word, k, l):
                        return True
                    board[k][l] = temp
                    word = a+word

        if j == len(board[0])-1:
            pass  # no right
        else:
            # right
            k = i
            l = j+1
            right = board[k][l]
            if right == word[0]:  # found first letter
                if len(word) == 1:
                    # found complete word
                    return True
                else:
                    a, word = word[0], word[1:]
                    temp = board[k][l]
                    board[k][l] = '0'
                    if self.dfs(board, word, k, l):
                        return True
                    board[k][l] = temp
                    word = a+word

        return False


# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
s = Solution().exist(board, word)
print(s)
