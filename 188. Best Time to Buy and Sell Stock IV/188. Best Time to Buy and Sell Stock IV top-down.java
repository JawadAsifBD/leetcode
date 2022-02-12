class Solution {
    private int k;
    private int[] prices;
    private int[][][] memo;

    private int dp(int i, int trxn_remaining, int holding) {
        // base case
        if (i == prices.length || trxn_remaining == 0) {
            return 0;
        }
        if (memo[i][trxn_remaining][holding] == 0) {
            int do_nothing = dp(i + 1, trxn_remaining, holding);
            int do_something = 0;

            if (holding == 1) {
                // sell stock
                do_something = prices[i] + dp(i + 1, trxn_remaining - 1, 0);
            } else {
                // buy stock
                do_something = -prices[i] + dp(i + 1, trxn_remaining, 1);
            }
            memo[i][trxn_remaining][holding] = Math.max(do_nothing, do_something);
        }
        return memo[i][trxn_remaining][holding];
    }

    public int maxProfit(int k, int[] prices) {
        this.k = k;
        this.prices = prices;
        this.memo = new int[prices.length][k + 1][2];

        return dp(0, k, 0);
    }
}