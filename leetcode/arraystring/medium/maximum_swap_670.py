class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [int(i) for i in str(num)]
        max = (-1,-1)
        max_right = [None] * len(num_list)
        for i in range(len(num_list)-1, -1, -1):
            if num_list[i] > max[0]:
                max = (num_list[i], i)

            max_right[i] = max

        for i in range(len(num_list)):
            if num_list[i] < max_right[i][0]:
                temp = num_list[i]
                num_list[i] = max_right[i][0]
                num_list[max_right[i][1]] = temp
                return int(''.join(map(str, num_list)))
        return int(''.join(map(str, num_list)))

solution = Solution()
solution.maximumSwap(2736)


