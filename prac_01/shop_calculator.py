

total_price = 0
"""Ask user to input number of items"""
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
# Ask user for price of each item
for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    """Sum the prices and print the result"""
    total_price += item_price
print("Total price for {{:.0f}} items is ${:.2f}".format(total_price).format(number_of_items))
