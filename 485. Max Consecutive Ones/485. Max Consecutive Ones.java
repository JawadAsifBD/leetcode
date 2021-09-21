class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int temp_result = 0;
        int result = 0;
        
        for(int i:nums) {
            if( i==1 ) {
                temp_result ++;
            }
            else {
                if(temp_result>result) {
                    result = temp_result;
                }
                temp_result = 0;
            }
        }
        if ( temp_result > result ) {
            result = temp_result;
        }
        return result;
    }
}