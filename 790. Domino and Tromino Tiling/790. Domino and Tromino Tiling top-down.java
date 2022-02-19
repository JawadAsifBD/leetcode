class Solution {
    private long[] memo;
    private long MOD = 1_000_000_007;

    private long dp(int i) {
        if (i <= 0) {
            return 0;
        }
        if (i == 1) {
            return 1;
        }
        if (i == 2) {
            return 2;
        }
        if (i == 3) {
            return 5;
        }
        if (memo[i] == 0) {
            memo[i] = ((2 * dp(i - 1) + dp(i - 3)) % MOD);
        }
        return memo[i];
    }

    public int numTilings(int n) {
        this.memo = new long[n + 1];
        return (int) (dp(n) % MOD);
    }
}