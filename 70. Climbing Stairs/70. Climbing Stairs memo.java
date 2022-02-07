class Solution {
    private HashMap<Integer,Integer> memo = new HashMap<>();
    private int dp(int i) {
        if (i <= 2) return i;
        if (!memo.containsKey(i)) {
            memo.put(i,dp(i-1)+dp(i-2));
        }
        return memo.get(i);
    }
    public int climbStairs(int n) {
        return dp(n);
    }
}