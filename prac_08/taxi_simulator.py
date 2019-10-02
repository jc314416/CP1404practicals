from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""
"Need to save each taxi for subsequent trips"
"Need to add flagfall if there is one"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    current_bill = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
            print("Bill to date: ${:.2f}".format(current_bill))
        elif choice == "d":
            if current_taxi is not None:
                current_taxi.start_fare()
                drive_taxi(current_taxi)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                current_bill += current_taxi.get_fare()
                print("Bill to date: ${:.2f}".format(current_bill))
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: {:.2f}".format(current_bill))
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def choose_taxi(taxis):
    print("Taxis available:")
    print_taxis(taxis)
    choice = int(input("Choose Taxi: "))
    taxi = taxis[choice]
    return taxi


def drive_taxi(taxi):
    distance = int(input("Drive how far? "))
    taxi.drive(distance)


main()
