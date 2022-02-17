class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if i == m:
                if k == 0:
                    return 0
                return float('inf')
            if k == 0:
                return float('inf')

            mincost = float('inf')

            if houses[i] != 0:
                if j != houses[i]:
                    return float('inf')
                for next_color in range(1, n+1):
                    if j == next_color:
                        mincost = min(mincost, dp(i+1, j, k))
                    else:
                        mincost = min(mincost, dp(i+1, next_color, k-1))
            else:
                for next_color in range(1, n+1):
                    if j == next_color:
                        mincost = min(mincost, cost[i][j-1] + dp(i+1, j, k))
                    else:
                        mincost = min(
                            mincost, cost[i][j-1] + dp(i+1, next_color, k-1))
            return mincost

        result = min([dp(0, color, target) for color in range(1, n+1)])
        return result if result != float('inf') else -1
