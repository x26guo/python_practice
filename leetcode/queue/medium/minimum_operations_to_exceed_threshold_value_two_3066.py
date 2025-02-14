import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        steps = 0
        heapq.heapify(nums)
        while True:
            if len(nums) == 1 or len(nums) == 0:
                break
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            if first >= k:
                break

            result = min(first, second) * 2 + max(first, second)
            heapq.heappush(nums, result)
            steps += 1

        return steps

solution = Solution()
nums = [2,11,10,1,3]
solution.minOperations(nums, 10)