from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(output: List[List[int]], current: List[int]):
            if len(current) == len(nums):
                output.append(current[:])

            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack(output, current)
                del current[-1]

        output = []
        backtrack(output, [])
        return output