# Time Complexity:
#   ~O(c^(v/a)) where
#       c = number of coins
#       v = target value
#       a = average coin worth
def coin_change_slow(coins, val):
    if val < 0: return -1        
    if val == 0: return 0

    ways = []
    for coin in coins:
        num_coins = coin_change_slow(coins, val - coin)
        if num_coins > -1: ways.append(num_coins + 1)
                
    if len(ways) > 0:
        return min(ways)
    else:
        return -1

# print(coin_change_slow([1, 2, 5], 11))

