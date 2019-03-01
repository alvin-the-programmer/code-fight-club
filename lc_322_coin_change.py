# Time Complexity:
#   ~O(c^(v/a)) where
#       c = number of coins
#       v = target value
#       a = average coin worth

# 1 - write the brute force code
# 2 - add the memo obj as another arg
# 3 - at the top, add a base case, if the input is in the memo, then return it
# 4 - when we make a recursive call, save the result in the memo

# print(coin_change_fast([1, 2, 5], 11))
# print(coin_change_fast([1, 10, 25], 100))


class Solution:
    def coinChange(self, coins: List[int], amount: int, memo={}) -> int:
        if amount < 0: return -1        
        if amount == 0: return 0
        if amount in memo: return memo[amount]

        ways = []
        for coin in coins:
            num_coins = self.coinChange(coins, amount - coin, memo)
            if num_coins > -1: ways.append(num_coins + 1)
    
        memo[amount] = min(ways) if len(ways) > 0 else -1
        return memo[amount]


