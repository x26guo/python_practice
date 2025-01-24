from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        num_arrows = 1
        target = points[0]
        for point in points:
            if point[0] > target[1]:
                num_arrows += 1
                target = point
        return num_arrows