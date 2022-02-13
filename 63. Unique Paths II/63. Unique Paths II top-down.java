class Solution {
    private int[][] memo, obstacleGrid;

    private int dp(int row, int column) {
        if (obstacleGrid[row][column] == 1) {
            return 0;
        }
        if (row + column == 0)
            return 1;
        if (memo[row][column] == 0) {
            int ways = 0;
            if (row > 0) {
                ways += dp(row - 1, column);
            }
            if (column > 0) {
                ways += dp(row, column - 1);
            }
            memo[row][column] = ways;
        }
        return memo[row][column];
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        this.obstacleGrid = obstacleGrid;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        this.memo = new int[m][n];
        return dp(m - 1, n - 1);
    }
}