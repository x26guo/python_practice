from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(output, current, n):
            output.append(current[:])
            for i in range(n, len(nums)):
                current.append(nums[i])
                backtrack(output, current, i+1)
                del current[len(current) - 1]


        output = []
        backtrack(output, [], 0)

        return output