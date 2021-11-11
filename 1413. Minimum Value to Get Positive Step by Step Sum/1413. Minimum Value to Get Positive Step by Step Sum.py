class Solution:
    def minStartValue(self, A: List[int]) -> int:
        Sum, ans = 0, 0
        for el in A:
            Sum = Sum + el
            ans = min(ans, Sum)
        return -ans + 1
