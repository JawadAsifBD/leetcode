import java.util.List;

class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (String word : wordDict) {
                // to get s.substring(i-word.length()+1,i), we need to have i -
                // (word.length()-1) >= 0
                // to get dp[i-word.length()], we need to have i - word.length() >= 0 =>
                // i>=word.length()
                if (i >= word.length() - 1 && (i == word.length() - 1 || dp[i - word.length()])) {
                    if (s.substring(i - word.length() + 1, i + 1).equals(word)) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        return dp[s.length() - 1];
    }
}