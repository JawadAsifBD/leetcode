class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(s.substring(i, i + 1));
            if (x >= 1 && x <= 9) {
                dp[i + 1] += dp[i];
            }
            if (i - 1 >= 0) {
                x = Integer.parseInt(s.substring(i - 1, i + 1));
                if (x >= 10 && x <= 26) {
                    dp[i + 1] += dp[i - 1];
                }
            }
        }
        return dp[n];
    }
}