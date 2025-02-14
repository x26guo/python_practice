class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(num: int) -> int:
            sum = 0
            while num // 10 > 0:
              sum += num % 10
              num = num // 10
            sum += num % 10
            return sum


        dic = {}
        for n in nums:
            sum_digits = sum_of_digits(n)
            if sum_digits in dic:
                if len(dic[sum_digits]) == 1:
                    if dic[sum_digits][0] < n:
                        dic[sum_digits].append(dic[sum_digits][0])
                        dic[sum_digits][0] = n
                    else:
                        dic[sum_digits].append(n)
                else:
                    if dic[sum_digits][0] < n:
                        dic[sum_digits][1] = dic[sum_digits][0]
                        dic[sum_digits][0] = n
                    elif dic[sum_digits][1] < n:
                        dic[sum_digits][1] = n
            else:
                dic[sum_digits] = []
                dic[sum_digits].append(n)
        max = -1
        for key in dic:
            if len(dic[key]) == 2:
                sum = dic[key][0] + dic[key][1]
                if sum > max:
                    max = sum
        return max
