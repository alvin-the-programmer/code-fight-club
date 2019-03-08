class Solution:
    def change(self, amount, coins, memo = None):
        # print(memo)
        if memo is None:
            memo = {}

        key = str(coins) + str(amount)

        if key in memo: 
            return memo[key]

        if amount == 0: return 1
        if len(coins) == 0: return 0

        last_coin = coins[-1]

        coin_ways = 0
        qty = 0
        while qty * last_coin <= amount:
            coin_ways += self.change(amount - (qty * last_coin), coins[:-1], memo)
            qty += 1

        memo[key] = coin_ways
        return memo[key]


amount = 10000
coins = [25, 10, 5, 1]
s = Solution()
print(s.change(amount, coins))

                
