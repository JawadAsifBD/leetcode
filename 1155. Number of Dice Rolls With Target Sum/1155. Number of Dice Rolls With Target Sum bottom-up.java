class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        int[][] dp = new int[n + 1][target + 1];
        int modulo = 1000000007;
        dp[0][0] = 1;
        for (int dice_left = 1; dice_left <= n; dice_left++) {
            for (int target_left = 1; target_left <= target; target_left++) {
                for (int i = 1; i <= Math.min(target_left, k); i++) {
                    dp[dice_left][target_left] += dp[dice_left - 1][target_left - i];
                    dp[dice_left][target_left] %= modulo;
                }
            }
        }
        return dp[n][target];
    }
}