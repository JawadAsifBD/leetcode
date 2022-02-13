class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];

        for (int row = 0; row < m; row++) {
            for (int column = 0; column < n; column++) {
                dp[row][column] += grid[row][column];
                if (row > 0 && column > 0) {
                    dp[row][column] += Math.min(dp[row - 1][column], dp[row][column - 1]);
                } else if (row > 0) {
                    dp[row][column] += dp[row - 1][column];
                } else if (column > 0) {
                    dp[row][column] += dp[row][column - 1];
                }
            }
        }
        return dp[m - 1][n - 1];
    }
}