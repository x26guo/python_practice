from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        cur = intervals[0]
        for i in range(1, len(intervals)):
            next = intervals[i]
            if cur[1] >= next[0]:
                cur[1] = max(cur[1], next[1])
            else:
                output.append(cur)
                cur = next
        output.append(cur)
        return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals))