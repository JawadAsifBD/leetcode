class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        for (int row = 0; row < m; row++) {
            for (int column = 0; column < n; column++) {
                if (obstacleGrid[row][column] == 1) {
                    dp[row][column] = 0;
                    continue;
                }
                if (row > 0) {
                    dp[row][column] += dp[row - 1][column];
                }
                if (column > 0) {
                    dp[row][column] += dp[row][column - 1];
                }
            }
        }
        return dp[m - 1][n - 1];
    }
}