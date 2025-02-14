class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0

        dp = [True] * (n)
        dp[0] = False
        dp[1] = False

        count_of_primes = 0
        for i in range(2, n):
            if not dp[i]:
                continue
            count_of_primes += 1
            start = 2
            while i * start < n:
                dp[i * start] = False
                start += 1

        return count_of_primes