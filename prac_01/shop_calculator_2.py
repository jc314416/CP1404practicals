

price_list = []
"""Ask user to input number of items"""
number_of_items = int(input("Enter number of items: "))
"""Ask user for price of each item"""
for i in range(0, number_of_items, 1):
    """Could put in formatting to increment item number when asking"""
    item_price = float(input("Enter item price: $"))
    price_list.append(item_price)
"""Sum the prices and print the result"""
total_price = sum(price_list)
for i in range(0, number_of_items, 1):
    print("Price of item: ${:.2f}".format(price_list[i]))
print("Total price for {{:.0f}} items is ${:.2f}".format(total_price).format(number_of_items))
