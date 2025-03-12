import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ""
        max_heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(max_heap, (count, char))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(output) > 1 and char == output[-1] == output[-2]:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                output += char2
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, char2))
            else:
                output += char
                count += 1

            if count:
                heapq.heappush(max_heap, (count, char))
        return output

