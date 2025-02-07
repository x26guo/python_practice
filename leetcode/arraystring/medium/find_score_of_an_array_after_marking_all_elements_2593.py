import collections
from queue import PriorityQueue
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                # use dic
                dic[nums[i]] = {}
            dic[nums[i]][i] = i

        sorted_dic = collections.OrderedDict(sorted(dic.items()))

        for key in sorted_dic:
            collections.OrderedDict(sorted(sorted_dic[key].items()))

        output = 0
        while sorted_dic:
            key = next(iter(sorted_dic))
            output += key
            min_index = next(iter(sorted_dic[key]))
            del sorted_dic[key][min_index]
            #mark middle
            if not sorted_dic[key]:
                del sorted_dic[key]
            #mark left
            left_index = min_index - 1
            if left_index >= 0 and nums[left_index] in sorted_dic:
                if nums[left_index] in sorted_dic and left_index in sorted_dic[nums[left_index]]:
                    del sorted_dic[nums[left_index]][left_index]
                    if not sorted_dic[nums[left_index]]:
                        del sorted_dic[nums[left_index]]
            #mark right
            right_index = min_index + 1
            if right_index < len(nums) and nums[right_index] in sorted_dic:
                if nums[right_index] in sorted_dic and right_index in sorted_dic[nums[right_index]]:
                    del sorted_dic[nums[right_index]][right_index]
                    if not sorted_dic[nums[right_index]]:
                        del sorted_dic[nums[right_index]]
        return output

solution = Solution()
nums = [2,1,3,4,5,2]
solution.findScore(nums)