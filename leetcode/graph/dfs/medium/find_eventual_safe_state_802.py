from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        output = []
        safe = {}

        def is_safe(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbour in graph[i]:
                if not is_safe(neighbour):
                    return False
            safe[i] = True
            return True

        for i in range(len(graph)):
            if is_safe(i):
                output.append(i)
        return output