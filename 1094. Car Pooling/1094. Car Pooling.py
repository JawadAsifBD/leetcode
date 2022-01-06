from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0 for _ in range(1001)]
        for passenger, start, end in trips:
            timeline[start] += passenger
            timeline[end] -= passenger

        passenger_in_car = 0
        for i in timeline:
            passenger_in_car += i
            if passenger_in_car > capacity:
                return False
        return True


s = Solution()
trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
capacity = 11
print(s.carPooling(trips, capacity))
