from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True

        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> bool:
            # i,j,k are index of s1,s2,s3 accordingly
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            if i < len(s1) and s1[i] == s3[k]:
                if dp(i+1, j, k+1):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dp(i, j+1, k+1):
                    return True
            if i == len(s1)-1 and j == len(s2)-1 and k == len(s3)-1:
                return True
            return False

        return dp(0, 0, 0)


s = Solution()
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))
