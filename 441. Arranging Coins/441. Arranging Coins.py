class Solution:
    def arrangeCoins(self, n: int) -> int:
        res =1
        while res*(res+1)<=2*n:
            res +=1
        res-=1
        return res
