from prac_06.car import Car

MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    car = Car(car_name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ")
    while choice != "q":
        if choice == "d":
            distance = get_distance()
            drive_car(car, distance)
        elif choice == "r":
            refuel_car(car)
        else:
            print("Invalid choice")
        print(car)
        print(MENU)
        choice = input("Enter your choice: ")
    print("Goodbye {}'s driver".format(car.name))


def get_distance():
    distance = int(input("How many km do you wish to drive? "))
    while distance < 0:
        print("Distance must be >= 0")
        distance = int(input("How many km do you wish to drive? "))
    return distance


def drive_car(car, distance):
    if car.fuel > distance:
        print("The car drove {}km".format(distance))
        car.drive(distance)
    else:
        print("The car drove {}km and ran out of fuel\n".format(car.fuel))
        car.drive(distance)


def refuel_car(car):
    fuel = int(input("How many units of fuel do you want to add to the car? "))
    while fuel < 0:
        print("Fuel amount must be >= 0")
        fuel = int(input("How many units of fuel do you want to add to the car? "))
    car.add_fuel(fuel)
    print("Added {} units of fuel.\n".format(fuel))

main()
