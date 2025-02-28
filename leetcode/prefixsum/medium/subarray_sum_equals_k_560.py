from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_table = {0:1,}
        sum = 0
        result = 0
        for i in range(len(nums)):
            sum += nums[i]
            key = sum - k
            if key in prefix_sum_table:
                result += prefix_sum_table[key]
            if sum in prefix_sum_table:
                prefix_sum_table[sum] = prefix_sum_table[sum] + 1
            else:
                prefix_sum_table[sum] = 1
        return result