import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "stock_prices.txt"
number_of_days=0
price = INITIAL_PRICE


# Open the file for writing
out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    # Generate a random integer of 1 or 2
    # If it's 1, the price increases; otherwise, it decreases
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Apply the price change
    price *= (1 + price_change)
    
    # Ensure price doesn't exceed the maximum or fall below the minimum
    if price < MIN_PRICE:
        price = MIN_PRICE
    elif price > MAX_PRICE:
        price = MAX_PRICE
    
    # Print the updated price
    number_of_days+=1
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)
    print(f"On day {number_of_days} price is: ${price:.2f}")

# Close the file
out_file.close()
