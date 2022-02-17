import java.util.Arrays;

class Solution {
    private int m, n, maxlen;
    private int[][] memo;
    private int[] nums1, nums2;

    private int dp(int i, int j) {
        if (i == m)
            return 0;
        if (j == n)
            return 0;

        if (memo[i][j + 1] == -1) {
            memo[i][j + 1] = dp(i, j + 1);
        }
        if (memo[i + 1][j] == -1) {
            memo[i + 1][j] = dp(i + 1, j);
        }
        if (memo[i][j] == -1) {
            if (nums1[i] == nums2[j]) {
                memo[i][j] = 1 + dp(i + 1, j + 1);
                maxlen = Math.max(maxlen, memo[i][j]);
            } else {
                memo[i][j] = 0;
            }
        }
        return memo[i][j];
    }

    public int findLength(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.m = nums1.length;
        this.n = nums2.length;
        this.maxlen = 0;
        this.memo = new int[m + 1][n + 1];
        for (int[] i : memo) {
            Arrays.fill(i, -1);
        }
        dp(0, 0);
        return maxlen;
    }
}