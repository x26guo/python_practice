class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [1]
        dic = {}
        output = []
        for c in s:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1


        cur_dic = {}
        counter = 0
        for c in s:
            if c in cur_dic:
                cur_dic[c] = cur_dic[c] + 1
            else:
                cur_dic[c] = 1
            if cur_dic[c] == dic[c]:
                counter = counter + cur_dic[c]
                del cur_dic[c]
            if not cur_dic:
                if counter != 0:
                    output.append(counter)
                    counter = 0
        return output
