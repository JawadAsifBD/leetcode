class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<>();

    private int dp(int n) {
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;
        if (n == 2)
            return 1;
        if (!memo.containsKey(n)) {
            memo.put(n, dp(n - 1) + dp(n - 2) + dp(n - 3));
        }
        return memo.get(n);
    }

    public int tribonacci(int n) {
        return dp(n);
    }
}