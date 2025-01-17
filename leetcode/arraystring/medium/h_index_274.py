from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        output = 0
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            index = i + 1
            if citations[i] >= index:
                output = index
        return output