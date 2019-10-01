from prac_06.guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
# name = input("Name: ")
# while name != "":
#     year = input("Year: ")
#     cost = input("Cost: ")
#     guitars.append(Guitar(name, year, cost))
#     name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "Vintage" if guitar.is_vintage() else ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
