from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        output = 1
        for i in range(len(nums) - 1, -1, -1):
            max = dp[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    val = 1 + dp[j]
                    if val > max:
                        max = val
            dp[i] = max
            if max > output:
                output = max
        return output

