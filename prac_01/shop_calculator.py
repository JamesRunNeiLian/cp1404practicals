number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price
# Apply discount if total price is over $100
if total_price > 100:
    discount = (0.1 * total_price)
    total_price = (total_price-discount)  # Apply 10% discount
# Format and display the total price
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
