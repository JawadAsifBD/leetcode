class Solution {
    private int[] days, costs, memo;
    private int n;

    private int dp(int day) {
        if (day > days[n - 1]) {
            return 0;
        }
        if (day == days[n - 1]) {
            return Math.min(Math.min(costs[0], costs[1]), costs[2]);
        }
        int i = 0;
        while (i < n && days[i] < day)
            i++;
        day = days[i];
        if (memo[day] == 0) {
            memo[day] = Math.min(Math.min(costs[0] +
                    dp(day + 1), costs[1] + dp(day + 7)), costs[2] + dp(day + 30));
        }
        return memo[day];
    }

    public int mincostTickets(int[] days, int[] costs) {
        this.days = days;
        this.costs = costs;
        this.n = days.length;
        this.memo = new int[366];
        return dp(days[0]);
    }
}