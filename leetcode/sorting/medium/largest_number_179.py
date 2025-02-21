from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)

        def compare(i1: str, i2: str):
            if i1 + i2 > i2 + i1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))

solution = Solution()
nums = [3,30,34,5,9]
solution.largestNumber(nums)
