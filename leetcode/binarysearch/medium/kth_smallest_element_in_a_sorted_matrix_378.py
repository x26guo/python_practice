from bisect import bisect_right
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r,N = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(m):
            cnt = 0
            for r in range(N):
                x = bisect_right(matrix[r],m)
                cnt += x
            return cnt

        while l < r:
            mid = l + (r - l) // 2
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l