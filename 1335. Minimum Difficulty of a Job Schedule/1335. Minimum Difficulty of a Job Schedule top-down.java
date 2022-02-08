class Solution {
    private int[] jobDifficulty;
    private int n;
    private int[][] memo;

    private int dp(int i, int day) {
        if (memo[i][day] == -1) {
            if (day == 1) {
                memo[i][day] = Arrays.stream(
                        Arrays.copyOfRange(jobDifficulty, i, n)).max().getAsInt();
            } else {
                int m = 300001;
                for (int j = 1; j < (n - i); j++) {
                    m = Math.min(m,
                            dp(i + j, day - 1)
                                    + Arrays.stream(Arrays.copyOfRange(jobDifficulty, i, i + j)).max().getAsInt());
                }
                memo[i][day] = m;
            }

        }
        return memo[i][day];

    }

    public int minDifficulty(int[] jobDifficulty, int d) {
        this.jobDifficulty = jobDifficulty;
        this.n = jobDifficulty.length;
        if (n < d)
            return -1;
        this.memo = new int[n][d + 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(this.memo[i], -1);
        }
        return dp(0, d);

    }
}