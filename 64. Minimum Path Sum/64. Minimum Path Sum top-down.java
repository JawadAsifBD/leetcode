class Solution {
    private int[][] memo, grid;

    private int dp(int row, int column) {
        if (row + column == 0)
            return grid[row][column];
        if (memo[row][column] == 0) {
            int ways = grid[row][column];
            if (row > 0 && column > 0) {
                ways += Math.min(dp(row - 1, column), dp(row, column - 1));
            } else if (row > 0) {
                ways += dp(row - 1, column);
            } else if (column > 0) {
                ways += dp(row, column - 1);
            }
            memo[row][column] = ways;
        }
        return memo[row][column];
    }

    public int minPathSum(int[][] grid) {
        this.grid = grid;
        int m = grid.length;
        int n = grid[0].length;
        this.memo = new int[m][n];
        return dp(m - 1, n - 1);
    }
}