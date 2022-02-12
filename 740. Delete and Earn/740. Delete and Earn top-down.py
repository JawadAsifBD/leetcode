from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        counter = Counter(nums)
        sorted_nums = sorted(counter)

        def dp(i: int) -> int:
            if i == 0:
                return sorted_nums[0]*counter[sorted_nums[0]]
            if i == 1:
                if sorted_nums[1] == sorted_nums[0]+1:
                    return max(sorted_nums[0]*counter[sorted_nums[0]], sorted_nums[1]*counter[sorted_nums[1]])
                else:
                    return sorted_nums[0]*counter[sorted_nums[0]]+sorted_nums[1]*counter[sorted_nums[1]]
            if i not in memo:
                if sorted_nums[i-1] == sorted_nums[i]-1:
                    memo[i] = max(
                        sorted_nums[i]*counter[sorted_nums[i]]+dp(i-2), dp(i-1))
                else:
                    memo[i] = sorted_nums[i] * \
                        counter[sorted_nums[i]]+dp(i-1)
            return memo[i]

        return dp(len(sorted_nums)-1)


s = Solution()
nums = [2, 2, 3, 3, 3, 4]
print(s.deleteAndEarn(nums))
