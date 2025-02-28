from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1

        output = []
        for n in nums:
            if dic[n] == 1 and (n-1 not in dic) and (n+1 not in dic):
                output.append(n)
        return output

