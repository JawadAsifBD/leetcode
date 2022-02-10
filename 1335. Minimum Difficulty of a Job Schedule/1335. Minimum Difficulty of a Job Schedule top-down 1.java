import java.util.Arrays;

class Solution {
    private int n, d;
    private int[][] memo;
    private int[] jobDifficulty, hardestJobRemaining;

    private int dp(int i, int day) {
        // base case
        if (day == d)
            return hardestJobRemaining[i];

        if (memo[i][day] == -1) {
            int hardest = 0;
            int best = Integer.MAX_VALUE;
            // recurrence relation
            for (int j = i; j < n - (d - day); j++) {
                hardest = Math.max(hardest, jobDifficulty[j]);
                best = Math.min(best, hardest + dp(j + 1, day + 1));
            }
            memo[i][day] = best;
        }

        return memo[i][day];

    }

    public int minDifficulty(int[] jobDifficulty, int d) {
        this.n = jobDifficulty.length;
        this.d = d;
        if (n < d)
            return -1;

        this.jobDifficulty = jobDifficulty;
        memo = new int[n][d + 1];
        hardestJobRemaining = new int[n];

        int hardest = 0;

        for (int i = n - 1; i >= 0; i--) {
            // set hardestJobRemaining
            hardest = Math.max(hardest, jobDifficulty[i]);
            hardestJobRemaining[i] = hardest;

            // fill memo with -1
            Arrays.fill(memo[i], -1);
        }

        return dp(0, 1);
    }
}