from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        output = []
        words2_dic = {}
        #merge
        for word in words2:
            dic_temp = self.convertStrToDic(word)
            for key in dic_temp:
                if key in words2_dic:
                    words2_dic[key] = max(dic_temp[key], words2_dic[key])
                else:
                    words2_dic[key] = dic_temp[key]


        for word in words1:
            word1_dic = self.convertStrToDic(word)
            isSubset = True
            for key in words2_dic:
                if key not in word1_dic or words2_dic[key] > word1_dic[key]:
                    isSubset = False
                    break
            if isSubset:
                output.append(word)
        return output

    def convertStrToDic(self, word: str) -> {}:
        dic = {}
        for c in word:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1
        return dic

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
solution = Solution()
print(solution.wordSubsets(words1, words2))