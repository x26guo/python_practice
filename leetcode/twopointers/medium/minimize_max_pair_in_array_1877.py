from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start = 0;
        end = len(nums) - 1
        pairs = []
        while start < end:
            pairs.append(nums[start] + nums[end])
            start = start + 1
            end = end - 1
        return max(pairs)

