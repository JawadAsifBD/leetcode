class Solution {
    private int[] nums, multipliers;
    private int[][] memo;
    private int n, m;

    private int dp(int i, int left) {
        if (i == m)
            return 0;

        int mult = multipliers[i];
        int right = n - 1 - (i - left);

        if (memo[i][left] == 0) {
            memo[i][left] = Math.max(mult * nums[left] + dp(i + 1, left + 1),
                    mult * nums[right] + dp(i + 1, left));
        }
        return memo[i][left];
    }

    public int maximumScore(int[] nums, int[] multipliers) {

        this.nums = nums;
        this.multipliers = multipliers;
        this.n = nums.length;
        this.m = multipliers.length;
        this.memo = new int[m][n];

        return dp(0, 0);

    }
}