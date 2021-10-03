public class Solution {
    public boolean canJump(int[] A) {
        boolean[] f = new boolean[A.length];
        f[0] = true;

        for (int i = 1; i < A.length; i++) {
            for (int j = 0; j < i; j++) {
                if (f[j] && j + A[j] >= i) {
                    f[i] = true;
                    break;
                }
            }
        }
        return f[A.length - 1];
    }
}