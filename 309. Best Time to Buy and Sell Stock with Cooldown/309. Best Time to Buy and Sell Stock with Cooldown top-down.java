class Solution {
    private int[] prices;
    private int[][] memo;

    private int dp(int i, int holding) {
        if (i >= prices.length)
            return 0;
        if (memo[i][holding] == 0) {
            int do_nothing = dp(i + 1, holding);
            int do_something = 0;
            if (holding == 1) {
                // sell stock
                do_something = prices[i] + dp(i + 2, 0);
            } else {
                // buy stock
                do_something = -prices[i] + dp(i + 1, 1);
            }
            memo[i][holding] = Math.max(do_nothing, do_something);
        }
        return memo[i][holding];
    }

    public int maxProfit(int[] prices) {
        this.prices = prices;
        this.memo = new int[prices.length][2];
        return dp(0, 0);
    }
}