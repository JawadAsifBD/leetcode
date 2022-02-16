class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[][] dp = new int[n + 1][2];

        for (int i = n - 1; i >= 0; i--) {
            for (int holding = 0; holding < 2; holding++) {
                int do_nothing = dp[i + 1][holding];
                int do_something = 0;
                if (holding == 1) {
                    // sell stock today
                    do_something = prices[i] - fee + dp[i + 1][0];
                } else {
                    // buy stock today
                    do_something = -prices[i] + dp[i + 1][1];
                }
                dp[i][holding] = Math.max(do_nothing, do_something);
            }
        }
        return dp[0][0];
    }
}