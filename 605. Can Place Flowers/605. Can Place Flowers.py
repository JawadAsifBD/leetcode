from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # if 0 at first position, next is also 0
                if i == 0 and (i+1 == len(flowerbed) or flowerbed[i+1] != 1):
                    n -= 1
                    flowerbed[i] = 1
                # if 0 at last position, previous is also 0
                elif i == len(flowerbed)-1 and (i == 0 or flowerbed[i-1] != 1):
                    n -= 1
                    flowerbed[i] = 1
                # normal cases, when 000, place '1' in the middle, 000 -> 010
                elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    n -= 1
                    flowerbed[i] = 1
            if n <= 0:
                return True

        return False


s = Solution()
# flowerbed, n = [1, 0, 0, 0, 1], 1
# flowerbed, n = [1, 0, 0, 0, 1], 2
# flowerbed, n = [1, 0, 0, 0, 0, 1], 2
flowerbed, n = [0, 0, 0, 0, 0, 1, 0, 0], 0
print(s.canPlaceFlowers(flowerbed, n))
