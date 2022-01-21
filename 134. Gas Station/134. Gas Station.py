from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate, debit, credit = None, 0, 0

        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                candidate, debit, credit = None, debit - credit, 0
            elif candidate is None:
                candidate = i

        return candidate if credit >= debit else -1


s = Solution()
gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
print(s.canCompleteCircuit(gas, cost))
