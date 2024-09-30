walmart_items = ["milk","redbull","juice","yogurt","chips"]
walmart_prices = [5.2,27.2,46.7,6.7,0.5]
for i in range(len(walmart_items)):
    print(f"I bought {walmart_items[i]} for ${walmart_prices[i]}")
total_price = 0

for price in walmart_prices:
    total_price = total_price + price
    print(total_price)

names = walmart_items[0]
cheapest= walmart_prices[0]
for i in range(len(walmart_prices)):
    if (walmart_prices[i] <= cheapest):
        cheapest = walmart_prices[i]
        name = walmart_items[i]
print(f"the cheapest item was {name}")

leastIndex = walmart_prices.index(min(walmart_prices))
print(f"the cheapest item was {walmart_items[leastIndex]}")