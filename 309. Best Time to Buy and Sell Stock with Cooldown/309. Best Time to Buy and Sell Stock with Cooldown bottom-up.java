class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n + 1][2];

        for (int i = n - 1; i >= 0; i--) {
            for (int holding = 0; holding <= 1; holding++) {
                int do_nothing = dp[i + 1][holding];
                int do_something = 0;
                if (holding == 1) {
                    // sell stock
                    do_something = i < n - 1 ? prices[i] + dp[i + 2][0] : prices[i];
                } else {
                    // buy stock
                    do_something = -prices[i] + dp[i + 1][1];
                }
                dp[i][holding] = Math.max(do_nothing, do_something);
            }
        }
        return dp[0][0];
    }
}