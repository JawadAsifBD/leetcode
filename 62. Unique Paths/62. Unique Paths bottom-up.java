class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for (int row = 0; row < m; row++) {
            for (int column = 0; column < n; column++) {
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