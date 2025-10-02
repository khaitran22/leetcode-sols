def maxProfit(prices):
    buy1 = -prices[0]
    sell1 = 0
    buy2 = -prices[0]
    sell2 = 0

    for i in range(1, len(prices)):
        price = prices[i]

        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2


prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(maxProfit(prices))
