from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        output = []
        l = 0
        r = len(nums) - 1
        while len(output) < len(nums):
            output.append(nums[l])
            l += 1

            if l <= r:
                output.append(nums[r])
                r -= 1
        return output