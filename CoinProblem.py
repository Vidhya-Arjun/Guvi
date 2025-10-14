def find_ways(total, coins, index=0, current=None):
    if current is None:
        current = []
    if total == 0:
        print(current)
        return
    if total < 0 or index >= len(coins):
        return

    # Include current coin
    find_ways(total - coins[index], coins, index, current + [coins[index]])

    # Exclude current coin and move to next
    find_ways(total, coins, index + 1, current)


coins = [1, 2, 5, 10]
find_ways(10, coins)