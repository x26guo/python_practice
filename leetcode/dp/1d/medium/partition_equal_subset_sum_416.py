class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for n in nums:
            sum += n
        if sum % 2 == 0:
            target = sum / 2
        else:
            return False

        dp = set()
        dp.add(0)
        for n1 in nums:
            if n1 == target:
                return True
            else:
                new_dp = set()
                for n2 in dp:
                    n = n1 + n2
                    if n == target: return True
                    if n not in dp:
                        new_dp.add(n)
                dp.update(new_dp)
        return False