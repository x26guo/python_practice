from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_pairs = len(skill) // 2
        dic = {}
        total_sum = 0
        for n  in skill:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
            total_sum += n

        if total_sum % num_pairs != 0:
            return -1

        sub_sum = total_sum // num_pairs

        pairs = []
        while dic:
            key = next(iter(dic))
            other = sub_sum - key
            if other in dic:
                pairs.append((key, other),)
                dic[key] = dic[key] - 1
                dic[other] = dic[other] - 1
                if dic[key] == 0:
                    del dic[key]
                if other in dic and dic[other] == 0:
                    del dic[other]
            else:
                return -1

        output = 0
        for t in pairs:
            output += t[0] * t[1]
        return output

solution = Solution()
skill = [3,2,5,1,3,4]
solution.dividePlayers(skill)