from prac_06.guitar import Guitar

guitars = []
# name = input("Name: ")
# while name != "":
#     year = input("Year: ")
#     cost = input("Cost: ")
#     guitars.append(Guitar(name, year, cost))
#     name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
for i, guitar in enumerate(guitars):
    vintage_string = "Vintage" if guitar.is_vintage() else ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
