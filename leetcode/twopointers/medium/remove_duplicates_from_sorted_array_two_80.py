from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            count = 1
            while fast < len(nums) - 1 and nums[fast] == nums[fast + 1]:
                fast += 1
                count += 1
            times = min(2, count)
            for i in range(times):
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow