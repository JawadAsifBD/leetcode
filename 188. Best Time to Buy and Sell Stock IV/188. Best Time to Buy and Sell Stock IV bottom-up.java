class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        int[][][] dp = new int[n + 1][k + 1][2];

        for (int i = n - 1; i >= 0; i--) {
            for (int trxn_remaining = 1; trxn_remaining <= k; trxn_remaining++) {
                for (int holding = 0; holding <= 1; holding++) {
                    int do_nothing = dp[i + 1][trxn_remaining][holding];
                    int do_something = 0;
                    if (holding == 1) {
                        // sell stock
                        do_something = prices[i] + dp[i + 1][trxn_remaining - 1][0];
                    } else {
                        // buy stock
                        do_something = -prices[i] + dp[i + 1][trxn_remaining][1];
                    }
                    dp[i][trxn_remaining][holding] = Math.max(do_nothing, do_something);
                }
            }
        }
        return dp[0][k][0];
    }
}