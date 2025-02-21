from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.output = nums[:]

    def reset(self) -> List[int]:
        self.output = self.original[:]
        return self.output

    def shuffle(self) -> List[int]:
        for i in range(len(self.output)):
            swap_index = random.randrange(i, len(self.output))
            temp = self.output[swap_index]
            self.output[swap_index] = self.output[i]
            self.output[i] = temp
        return self.output