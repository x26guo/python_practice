import math


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_count = self.count_number_of_one(num1)
        num2_count = self.count_number_of_one(num2)

        x = num1
        ## remove ones
        i = 0
        while num1_count > num2_count:
            power = (1 << i)
            if x & power != 0:
                x = (x ^ power)
                num1_count = num1_count - 1
            i += 1
        ## add ones
        i = 0
        while num1_count < num2_count:
            power = (1 << i)
            if x & power == 0:
                x = (x | power)
                num1_count = num1_count + 1
            i += 1
        return x


    def count_number_of_one(self, number) -> int:
        output = 0
        while number > 0:
            output = output + (number & 1)
            number = number >> 1
        return output


solution = Solution()
print(solution.minimizeXor(3,5))
print(solution.minimizeXor(1,12))
print(solution.minimizeXor(25,72))
print(solution.minimizeXor(79,74))
print(solution.minimizeXor(91,18))