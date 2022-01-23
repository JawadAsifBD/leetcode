from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque()
        for i in range(1, 10):
            queue.append(i)

        res = []
        while queue:
            u = queue.popleft()
            if low <= u <= high:
                res.append(u)
            if u > high:
                break
            last_num = u % 10
            if last_num != 9:
                queue.append(u * 10 + last_num + 1)

        return res


s = Solution()
low = 100
high = 300
print(s.sequentialDigits(low, high))
