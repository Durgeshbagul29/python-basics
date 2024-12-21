# If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred.

cost_price = float(input("Enter cost price: "))
sell_price = float(input("Enter selling price: "))

if sell_price > cost_price:
  profit = sell_price - cost_price
  print("We have profit here for ", profit, "rs")
elif sell_price < cost_price:
  loss = cost_price - sell_price
  print("We have loss for", loss, "rs")
else:
  print("We have no profit and no loss.")