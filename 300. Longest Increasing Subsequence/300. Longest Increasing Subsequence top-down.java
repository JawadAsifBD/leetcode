class Solution {
    private int[] nums, memo;

    private int dp(int i) {
        if (i == 0) {
            return 1;
        }
        if (memo[i] == 0) {
            int res = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    res = Math.max(res, 1 + dp(j));
                }
            }
            memo[i] = res;
        }
        return memo[i];
    }

    public int lengthOfLIS(int[] nums) {
        this.nums = nums;
        this.memo = new int[nums.length];
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res = Math.max(res, dp(i));
        }
        return res;
    }
}