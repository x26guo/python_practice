from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #example 1 3 5 4 3 2 1
        #output  1 4 1 2 3 3 5

        # find pivot which is 5
        pivot = 0

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return

        ## swap
        swap = len(nums) - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        nums[pivot - 1], nums[swap] = nums[swap], nums[pivot - 1]
        nums[pivot:] = sorted(nums[pivot:])
