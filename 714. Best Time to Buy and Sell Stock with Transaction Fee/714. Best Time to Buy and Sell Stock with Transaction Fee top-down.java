class Solution {
    private int n, fee;
    private int[] prices;
    private int[][] memo;

    private int dp(int i, int holding) {
        if (i == n)
            return 0;
        if (memo[i][holding] == 0) {
            int do_nothing = dp(i + 1, holding);
            int do_something = 0;
            if (holding == 1) {
                // sell stock today
                do_something = prices[i] - fee + dp(i + 1, 0);
            } else {
                // buy stock today
                do_something = -prices[i] + dp(i + 1, 1);
            }
            memo[i][holding] = Math.max(do_nothing, do_something);
        }
        return memo[i][holding];
    }

    public int maxProfit(int[] prices, int fee) {
        this.prices = prices;
        this.fee = fee;
        this.n = prices.length;
        this.memo = new int[n][2];
        return dp(0, 0);
    }
}