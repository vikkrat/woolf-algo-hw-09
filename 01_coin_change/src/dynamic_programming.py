def find_min_coins(amount, coins):
    dp = [0] + [float('inf')] * amount  # Initialize the dp array
    coin_used = [0] * (amount + 1)  # Track the coins used

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Reconstruct the coin combination from the coin_used array
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
