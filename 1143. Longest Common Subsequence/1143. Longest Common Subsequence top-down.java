class Solution {
    private String text1, text2;
    private int[][] memo;
    private int m, n;

    private int dp(int i, int j) {
        if (i == m)
            return 0;
        if (j == n)
            return 0;
        if (memo[i][j] == 0) {
            if (text1.charAt(i) == text2.charAt(j)) {
                memo[i][j] = 1 + dp(i + 1, j + 1);
            } else {
                memo[i][j] = Math.max(dp(i, j + 1), dp(i + 1, j));
            }
        }
        return memo[i][j];
    }

    public int longestCommonSubsequence(String text1, String text2) {
        this.text1 = text1;
        this.text2 = text2;
        this.m = text1.length();
        this.n = text2.length();
        this.memo = new int[m][n];
        return dp(0, 0);
    }
}