from math import floor
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        temp_max_dist_btwn_2_person = 0
        start_index = -1
        distance = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                temp_max_dist_btwn_2_person += 1
            else:
                if start_index == -1:
                    temp_distance = temp_max_dist_btwn_2_person
                    distance = max(distance, temp_distance)
                else:
                    temp_distance = temp_max_dist_btwn_2_person//2 + temp_max_dist_btwn_2_person % 2
                    distance = max(distance, temp_distance)
                temp_max_dist_btwn_2_person = 0
                start_index = i

        if seats[-1] == 0:  # last index is zero
            temp_distance = len(seats)-start_index-1
            distance = max(distance, temp_distance)
        return distance


s = Solution()
# seats = [1, 0, 0, 0, 1, 0, 1]
# seats = [1, 0, 0, 0]
# seats = [0, 1]
# seats = [1, 0, 0, 1]
seats = [0, 1, 0, 1, 0]
print(s.maxDistToClosest(seats))
