from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            next_index = i + nums[i]
            if next_index >= (len(nums) - 1):
                dp[i] = True
            else:
                for j in range(1, nums[i] + 1):
                    dp[i] = dp[i + j] or dp[i]
                    if dp[i]: break
        return dp[0]