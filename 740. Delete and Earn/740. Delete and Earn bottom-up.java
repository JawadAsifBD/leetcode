class Solution {
    public int deleteAndEarn(int[] nums) {
        int[] count = new int[10001];
        for (int x : nums)
            count[x]++;

        int prev = -1, avoid = 0, using = 0;

        for (int i = 0; i <= 10000; i++)
            if (count[i] > 0) {
                int m = Math.max(avoid, using);
                if (i - 1 == prev) {
                    using = i * count[i] + avoid;
                    avoid = m;
                } else {
                    using = i * count[i] + m;
                    avoid = m;
                }
                prev = i;
            }
        return Math.max(avoid, using);
    }
}