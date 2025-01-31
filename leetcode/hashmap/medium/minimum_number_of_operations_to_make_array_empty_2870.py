from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1

        steps = 0
        desc_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        while desc_dict:
            key = next(iter(desc_dict))
            val = desc_dict[key]
            if val % 3 == 0 or (val > 3 and (val - 3) % 2 == 0):
                steps += 1
                desc_dict[key] = desc_dict[key] - 3
            elif val % 2 == 0:
                steps += 1
                desc_dict[key] = desc_dict[key] - 2
            else:
                return -1
            if desc_dict[key] == 0:
                del desc_dict[key]

        return steps

solution = Solution()
#nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
solution.minOperations(nums)