class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                res = res + 4
                if j > 0:
                    # check left
                    if grid[i][j-1] == 1:
                        res = res - 2
                if i > 0:
                    # check up
                    if grid[i-1][j] == 1:
                        res = res - 2
        return res
