import java.util.Arrays;

class Solution {
    private int n;
    private int[] coins;
    private int[][] memo;

    private int dp(int amount, int coin_index) {
        if (amount < 0 || coin_index >= n) {
            return 0;
        }
        if (amount == 0) {
            return 1;
        }
        if (memo[amount][coin_index] == -1) {
            int take = dp(amount - coins[coin_index], coin_index);
            int notake = dp(amount, coin_index + 1);
            memo[amount][coin_index] = take + notake;
        }
        return memo[amount][coin_index];
    }

    public int change(int amount, int[] coins) {
        this.coins = coins;
        this.n = coins.length;
        this.memo = new int[amount + 1][coins.length];
        for (int[] arr : memo)
            Arrays.fill(arr, -1);
        return dp(amount, 0);
    }
}