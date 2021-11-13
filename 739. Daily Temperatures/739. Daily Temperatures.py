from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


s = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temperatures))
