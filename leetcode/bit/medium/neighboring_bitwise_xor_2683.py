from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        output = [None] * len(derived)
        output[0] = True
        for i in range(len(derived)):
            if i == len(derived) - 1:
                return output[i] ^ True == derived[i]
            if derived[i] == 1:
                output[i+1] = not output[i]
            else:
                output[i+1] = output[i]
