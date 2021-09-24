class Solution:
    def tribonacci(self, n: int) -> int:
        result = []
        result.append(0)
        result.append(1)
        result.append(1)

        if n < 3:
            return result[n]
        else:
            for i in range(3, n+1):
                result.append(result[i-3]+result[i-2]+result[i-1])
            return result[n]
