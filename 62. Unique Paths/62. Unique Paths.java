class Solution {
    public int uniquePaths(int m, int n) {
        int[][] matrix = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0) {
                    matrix[i][j] = 1;
                    continue;
                }
                if (j == 0) {
                    matrix[i][j] = 1;
                    continue;
                }
                int up = matrix[i - 1][j];
                int left = matrix[i][j - 1];
                matrix[i][j] = up + left;
            }
        }
        return matrix[m - 1][n - 1];
    }
}