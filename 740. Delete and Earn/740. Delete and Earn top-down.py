from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        nums_counter = Counter(nums)
        sorted_num_elements = sorted(nums_counter)

        def dp(i: int) -> int:
            if i == 0:
                return sorted_num_elements[0]*nums_counter[sorted_num_elements[0]]
            if i == 1:
                if sorted_num_elements[1] == sorted_num_elements[0]+1:
                    return max(sorted_num_elements[0]*nums_counter[sorted_num_elements[0]], sorted_num_elements[1]*nums_counter[sorted_num_elements[1]])
                else:
                    return sorted_num_elements[0]*nums_counter[sorted_num_elements[0]]+sorted_num_elements[1]*nums_counter[sorted_num_elements[1]]
            if i not in memo:
                if sorted_num_elements[i-1] == sorted_num_elements[i]-1:
                    memo[i] = max(
                        sorted_num_elements[i]*nums_counter[sorted_num_elements[i]]+dp(i-2), dp(i-1))
                else:
                    memo[i] = sorted_num_elements[i] * \
                        nums_counter[sorted_num_elements[i]]+dp(i-1)
            return memo[i]

        return dp(len(sorted_num_elements)-1)


s = Solution()
nums = [2, 2, 3, 3, 3, 4]
print(s.deleteAndEarn(nums))
