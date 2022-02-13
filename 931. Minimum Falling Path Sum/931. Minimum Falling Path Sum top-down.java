class Solution {
    private int[][] memo, matrix;
    private int m, n;

    private int dp(int row, int column) {
        int ways = matrix[row][column];
        if (row == 0) {
            return ways;
        }
        if (memo[row][column] == 0) {
            if (column > 0 && column < n - 1) {
                ways += Math.min(
                        dp(row - 1, column - 1), Math.min(dp(row - 1, column), dp(row - 1, column + 1)));
            } else if (column > 0) {
                ways += Math.min(
                        dp(row - 1, column - 1), dp(row - 1, column));
            } else if (column < n - 1) {
                ways += Math.min(
                        dp(row - 1, column), dp(row - 1, column + 1));
            }
            memo[row][column] = ways;
        }
        return memo[row][column];
    }

    public int minFallingPathSum(int[][] matrix) {
        this.matrix = matrix;
        this.m = matrix.length;
        this.n = matrix[0].length;
        this.memo = new int[m][n];
        for (int i = 0; i < n; i++) {
            memo[0][i] = matrix[0][i];
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, dp(m - 1, i));
        }
        return min;
    }
}