def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # sort in descending order
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result


# Example
coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
amount = 93
print("Coins used:", coin_change_greedy(coins, amount))