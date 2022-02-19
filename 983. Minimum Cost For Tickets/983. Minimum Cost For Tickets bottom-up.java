import java.util.Arrays;

class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[days[days.length - 1] + 1];
        for (int i = 0; i < dp.length; i++) {
            if (Arrays.binarySearch(days, i) >= 0) {
                dp[i] = Math.min(costs[0] + dp[Math.max(0, i - 1)],
                        Math.min(costs[1] + dp[Math.max(0, i - 7)],
                                costs[2] + dp[Math.max(0, i - 30)]));
            } else {
                dp[i] = dp[Math.max(i - 1, 0)];
            }
        }
        return dp[days[days.length - 1]];
    }
}