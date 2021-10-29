from typing import List
from itertools import product
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        m = len(grid)
        n = len(grid[0])
        rottenTimes = [[-1 for _ in range(n)] for _ in range(m)]
        # print(rottenTime)
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 2:  # rotten
                # print(i, j)
                queue.append((i, j, 0))
                rottenTimes[i][j] = 0

        while len(queue) != 0:
            i, j, rottentime = queue.popleft()
            # check left
            # grid[i][j] == 0 for no apple
            if j > 0 and grid[i][j-1] != 0 and rottenTimes[i][j-1] == -1:
                queue.append((i, j-1, rottentime+1))
                rottenTimes[i][j-1] = rottentime + 1
            # check right
            if j < n-1 and grid[i][j+1] != 0 and rottenTimes[i][j+1] == -1:
                queue.append((i, j+1, rottentime+1))
                rottenTimes[i][j+1] = rottentime + 1
            # check up
            if i > 0 and grid[i-1][j] != 0 and rottenTimes[i-1][j] == -1:
                queue.append((i-1, j, rottentime+1))
                rottenTimes[i-1][j] = rottentime + 1
            # check down
            if i < m-1 and grid[i+1][j] != 0 and rottenTimes[i+1][j] == -1:
                queue.append((i+1, j, rottentime+1))
                rottenTimes[i+1][j] = rottentime + 1
        # print(rottenTimes)

        max = 0
        for i, j in product(range(m), range(n)):
            if rottenTimes[i][j] > max:
                max = rottenTimes[i][j]
            if rottenTimes[i][j] == -1 and grid[i][j] != 0:
                return -1
        return max


# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# grid = [[0, 2]]
grid = [[0, 0, 0, 0]]
s = Solution()
print(s.orangesRotting(grid))
