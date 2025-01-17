from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common_dic = {}
        a_store = {}
        b_store = {}
        output = []
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            a_store[a] = 1
            b_store[b] = 1
            if (a not in common_dic) and (a in b_store):
                common_dic[a] = 1
            if (b not in common_dic) and (b in a_store):
                common_dic[b] = 1
            output.append(len(common_dic))
        return output