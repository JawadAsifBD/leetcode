import java.util.ArrayList;
import java.util.Stack;

class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        Stack<Integer> inconsistant_even = new Stack<>();
        Stack<Integer> inconsistant_odd = new Stack<>();

        for (int i = 0; i < nums.length; i++) {
            if (i % 2 != nums[i] % 2) {
                // inconsistant
                if (nums[i] % 2 == 1) {
                    // odd
                    if (inconsistant_even.size() > 0) {
                        // there is an even number in inconsistant array
                        // swap
                        int index = inconsistant_even.pop();
                        int temp = nums[index];
                        nums[index] = nums[i];
                        nums[i] = temp;
                    } else {
                        inconsistant_odd.push(i);
                    }
                } else {
                    // even number
                    if (inconsistant_odd.size() > 0) {
                        // there is an even number in inconsistant array
                        // swap
                        int index = inconsistant_odd.pop();
                        int temp = nums[index];
                        nums[index] = nums[i];
                        nums[i] = temp;
                    } else {
                        inconsistant_even.push(i);
                    }
                }
            }
        }
        return nums;
    }
}

public class a {
    public static void main(String args[]) {
        Solution s = new Solution();
        int[] res = { 648, 831, 560, 986, 192, 424, 997, 829, 897, 843 };
        s.sortArrayByParityII(res);
        for (int i : res) {
            System.out.print(i + " ");
        }
    }
}