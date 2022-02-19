class Solution {
    private String s1, s2, s3;
    private int[][][] memo;

    private boolean dp(int i, int j, int k) {
        if (memo[i][j][k] == -1) {
            if (k == s3.length()) {
                if (i == s1.length() && j == s2.length()) {
                    memo[i][j][k] = 1;
                    return true;
                }
                memo[i][j][k] = 0;
                return false;
            }
            if (i < s1.length() && s1.charAt(i) == s3.charAt(k)) {
                if (dp(i + 1, j, k + 1)) {
                    memo[i][j][k] = 1;
                }
            }
            if (j < s2.length() && s2.charAt(j) == s3.charAt(k)) {
                if (dp(i, j + 1, k + 1)) {
                    memo[i][j][k] = 1;
                }
            }
            if (memo[i][j][k] == -1) {
                memo[i][j][k] = 0;
            }
        }
        return memo[i][j][k] == 1 ? true : false;
    }

    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        if (s1.length() == 0 && s2.length() == 0 && s3.length() == 0) {
            return true;
        }
        this.s1 = s1;
        this.s2 = s2;
        this.s3 = s3;
        this.memo = new int[s1.length() + 1][s2.length() + 1][s3.length() + 1];
        for (int[][] i : memo) {
            for (int[] j : i) {
                Arrays.fill(j, -1);
            }
        }
        return dp(0, 0, 0);
    }
}
