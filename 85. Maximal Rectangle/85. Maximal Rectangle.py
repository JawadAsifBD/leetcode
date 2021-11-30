class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROW, COL = len(matrix), len(matrix[0])
        dph = [[0]*COL for _ in range(1+ROW)]
        dpl = [[0]*COL for _ in range(1+ROW)]
        dpr = [[COL-1]*COL for _ in range(1+ROW)]
        for i in range(1, 1+ROW):
            lb, ub = 0, COL-1
            for j in range(COL):
                if matrix[i-1][j] == "1":
                    dph[i][j] = 1+dph[i-1][j]
                    dpl[i][j] = max(lb, dpl[i-1][j])
                else:
                    lb = j+1
            for j in reversed(range(COL)):
                if matrix[i-1][j] == "1":
                    dpr[i][j] = min(ub, dpr[i-1][j])
                else:
                    ub = j-1
        maxArea = 0
        for i in range(1, 1+ROW):
            for j in range(COL):
                maxArea = max(maxArea, (dpr[i][j]-dpl[i][j]+1)*dph[i][j])
        return maxArea
