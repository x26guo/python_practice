from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1: return 0;

        dp = [None] * len(nums)
        dp[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i] >= len(nums) - 1):
                dp[i] = 1
            else:
                minimum = float('inf')
                for j in range(nums[i]):
                    index = i + j + 1
                    if index > len(nums) - 1:
                        break
                    if dp[index] == 0:
                        continue

                    minimum = min(dp[index], minimum)
                if minimum == float('inf'):
                    dp[i] = 0
                else:
                    dp[i] = minimum + 1


        return dp[0]