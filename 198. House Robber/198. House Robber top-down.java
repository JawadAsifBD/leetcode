class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<>();
    private int[] nums;

    private int dp(int i) {
        if (i == 0)
            return nums[0];
        if (i == 1)
            return Math.max(nums[0], nums[1]);
        if (!memo.containsKey(i)) {
            memo.put(i, Math.max(dp(i - 1), nums[i] + dp(i - 2)));
        }
        return memo.get(i);
    }

    public int rob(int[] nums) {
        this.nums = nums;
        return dp(nums.length - 1);
    }
}