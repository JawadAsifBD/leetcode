import java.util.Arrays;

class Solution {
    private int[][] memo;
    private int k, modulo = 1000000007;

    private int dp(int dice_left, int target_left) {
        if (dice_left == 0) {
            if (target_left == 0) {
                return 1;
            }
            return 0;
        }
        if (memo[dice_left][target_left] == -1) {
            int res = 0;
            for (int i = 1; i <= Math.min(k, target_left); i++) {
                res += dp(dice_left - 1, target_left - i);
                res %= modulo;
            }
            memo[dice_left][target_left] = res;
        }
        return memo[dice_left][target_left];
    }

    public int numRollsToTarget(int n, int k, int target) {
        this.k = k;
        this.memo = new int[n + 1][target + 1];
        for (int[] i : memo) {
            Arrays.fill(i, -1);
        }
        return dp(n, target);
    }
}