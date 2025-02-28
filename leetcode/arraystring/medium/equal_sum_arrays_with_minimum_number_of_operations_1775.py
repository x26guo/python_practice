from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(n1: List[int], n2: List[int]) -> int:
            n1 = sorted(n1)
            n2 = sorted(n2, reverse=True)
            target = sum(n2) - sum(n1)
            i_1 = 0
            i_2 = 0
            output = 0
            while True:
                diff = 0
                if i_1 > len(n1) - 1 and i_2 > len(n2) - 1:
                    break
                elif i_1 > len(n1) - 1:
                    diff = n2[i_2] - 1
                    i_2 += 1
                elif i_2 > len(n2) - 1:
                    diff = 6 - n1[i_1]
                    i_1 += 1
                else:
                    if (n2[i_2] - 1) > (6 - n1[i_1]):
                        diff = n2[i_2] - 1
                        i_2 += 1
                    else:
                        diff = 6 - n1[i_1]
                        i_1 += 1
                if target < diff:
                    return output + 1
                target -= diff
                output += 1
            return -1


        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 == sum2: return 0
        output = 0
        if sum1 < sum2:
            output = helper(nums1, nums2)
        else:
            output = helper(nums2, nums1)
        return output



solution = Solution()
nums1 = [6,6]
nums2 = [1]
solution.minOperations(nums1,nums2)