class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = {}

        for c in s1:
            if c in s1_dic:
                s1_dic[c] = s1_dic[c] + 1
            else:
                s1_dic[c] = 1

        s1_dic_clone = s1_dic.copy()
        slow = 0
        fast = 0
        while fast < len(s2):
            ch = s2[fast]
            if ch in s1_dic_clone:
                fast += 1
                s1_dic_clone[ch] = s1_dic_clone[ch] - 1
                if s1_dic_clone[ch] == 0:
                    del s1_dic_clone[ch]
                if not s1_dic_clone:
                    return True
            else:
                slow += 1
                fast = slow
                s1_dic_clone = s1_dic.copy()

        return False