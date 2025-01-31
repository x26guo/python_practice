from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                pre = i - coin
                if pre >= 0:
                    if dp[pre] >= 0:
                        if dp[i] < 0:
                            dp[i] = dp[pre] + 1
                        else:
                            dp[i] = min(dp[pre] + 1, dp[i])
        return dp[-1]

solution = Solution()
coins = [1,2,5]
amount = 11
solution.coinChange(coins, amount)