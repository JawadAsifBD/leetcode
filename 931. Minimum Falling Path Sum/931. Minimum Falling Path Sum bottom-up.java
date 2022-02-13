class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m][n];

        for (int i = 0; i < n; i++) {
            dp[0][i] = matrix[0][i];
        }
        for (int row = 1; row < m; row++) {
            for (int column = 0; column < n; column++) {
                dp[row][column] += matrix[row][column];
                if (column > 0 && column < n - 1) {
                    dp[row][column] += Math.min(dp[row - 1][column - 1],
                            Math.min(dp[row - 1][column], dp[row - 1][column + 1]));
                } else if (column > 0) {
                    dp[row][column] += Math.min(
                            dp[row - 1][column - 1], dp[row - 1][column]);
                } else if (column < n - 1) {
                    dp[row][column] += Math.min(
                            dp[row - 1][column], dp[row - 1][column + 1]);
                }
            }
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, dp[m - 1][i]);
        }
        return min;
    }
}