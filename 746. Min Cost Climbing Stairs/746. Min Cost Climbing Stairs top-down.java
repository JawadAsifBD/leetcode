class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<>();
    private int[] cost;

    private int dp(int i) {
        if (i <= 1)
            return 0;
        if (!memo.containsKey(i)) {
            memo.put(i, Math.min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2)));
        }
        return memo.get(i);
    }

    public int minCostClimbingStairs(int[] cost) {
        this.cost = cost;
        return dp(cost.length);
    }
}