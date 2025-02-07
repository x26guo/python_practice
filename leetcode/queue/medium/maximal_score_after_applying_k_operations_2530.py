import math
from queue import PriorityQueue
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        queue = PriorityQueue()
        score = 0
        for n in nums:
            queue.put(-n)

        while k > 0:
            largest = queue.get()
            largest = -largest
            score += largest
            k -= 1
            largest = math.ceil(largest / 3)
            queue.put(-largest)
        return score
