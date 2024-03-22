
# List of keys/menu items
cafe_menu = ['espresso', 'muffins', 'cookies', 'tea']
# Dictionary of amounts of each items in stock
cafe_stock = {'espresso': 85, 'muffins': 15, 'cookies': 30, 'tea': 60}
# Dictionary of stock items and their prices
unit_price = {'espresso': 2, 'muffins': 3.5, 'cookies': 2.5, 'tea': 3}

# Creates a price variable to receive the total prices
total_price = 0

# For loop that iterates through the menu list, using each item as keys for the stock and price dictionaries
for item in cafe_menu:
    # The loop then multiplies each stock amount and price before adding it to the total price variable
    total_price = total_price + cafe_stock[item]*unit_price[item]

# Prints out the total price calculated by the loop
print("The total price of the cafe's stock is: " + str(total_price))