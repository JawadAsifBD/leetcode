class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        for(int i=0; i<shifts.length; i++) {
            shifts[i] = shifts[i]%26;
        }
        int[] finalshifts = shifts.clone();
        
        int sum = 0;
        for(int i = finalshifts.length-1; i>=0; i--) {
            finalshifts[i] = (finalshifts[i] + sum)%26;
            sum += shifts[i];
        }
        char[] result = s.toCharArray();
        for(int i=0; i<result.length; i++ ) {
            result[i] += finalshifts[i];
            result[i] = (char)(((result[i]-'a') % 26) + 'a');
        }
        return String.valueOf(result);
    }
}

public class shifting_letters {
    public static void main(String[] args) {
        String str = "mkgfzkkuxownxvfvxasy";
        int[] shifts = {505870226,437526072,266740649,224336793,532917782,311122363,567754492,595798950,81520022,684110326,137742843,275267355,856903962,148291585,919054234,467541837,622939912,116899933,983296461,536563513};
        Solution s = new Solution();
        String str1 = s.shiftingLetters(str,shifts);
        System.out.println(str1);
    }
}