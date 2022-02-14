class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            return int(target <= k)
        '''
        def dp(remaining, needed):
            if remaining == 1 and (needed <= k and needed >= 1):
                return 1
            count = 0
            limit_ = min(k, needed)
            for num in range(1, limit_+1):
                #if needed - num > 0:
                count += dp(remaining - 1, needed - num)
            return count % (10 ** 9 + 7)
        return dp(n, target)
        '''
        modulo = 10 ** 9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(1, min(k, target) + 1):
            dp[1][i] = 1
        for remaining in range(2, n+1):
            for needed in range(target, -1, -1):
                count = 0
                limit_ = min(k, needed)
                for num in range(1, limit_+1):
                    count += dp[remaining - 1][needed - num]
                dp[remaining][needed] = count % (modulo)
        return dp[n][target]
