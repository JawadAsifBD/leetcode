from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for customer_accounts in accounts:
            res = max(res, sum(customer_accounts))
        return res


s = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(s.maximumWealth(accounts))
