# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


import sys


class Solution:
    def coinChange(self, coins, amount):
        inf = amount + 1
        coins.sort()
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        # print(dp)

        for i in range(n + 1):
            for j in range(amount + 1):
                if i == 0:
                    dp[i][j] = inf
                elif j == 0:
                    dp[i][j] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if coins[i - 1] <= j:
                    prev_step = dp[i][j - coins[i - 1]]
                    dp[i][j] = (
                        inf
                        if (dp[i][j] == inf and prev_step == inf)
                        else min(prev_step + 1, dp[i][j])
                    )

        for i in range(n + 1):
            print(dp[i])

        sol = min(dp[i][amount] for i in range(n + 1))
        return sol if sol != inf else -1

    def coinChange2(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for amt in range(1, amount + 1):
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


sol = Solution()
coins = [2, 5]
amount = 21
print(sol.coinChange2(coins, amount))
