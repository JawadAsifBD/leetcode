import java.util.TreeSet;

class Solution {
    public int minimumDeviation(int[] nums) {
        TreeSet<Integer> ts = new TreeSet<>();

        for (int i : nums) {
            if (i % 2 == 1)
                i *= 2;
            ts.add(i);
        }

        int diff = Integer.MAX_VALUE;
        while (true) {
            int max = ts.last();
            int min = ts.first();
            diff = Math.min(diff, max - min);
            if (max % 2 == 0) {
                ts.remove(max);
                max /= 2;
                ts.add(max);
            } else {
                break;
            }
        }
        return diff;
    }
}