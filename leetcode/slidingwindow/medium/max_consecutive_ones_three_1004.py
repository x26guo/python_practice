from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        fast = 0
        max_length = 0
        while fast < len(nums):
            if nums[fast] == 1:
                if (fast - slow + 1) > max_length:
                    max_length = fast - slow + 1
                fast += 1
            else:
                 if k > 0:
                     k -= 1
                     if (fast - slow + 1) > max_length:
                         max_length = fast - slow + 1
                     fast += 1
                 else:
                    while k <= 0:
                        if nums[slow] == 0:
                            k += 1
                        slow += 1
        return max_length

