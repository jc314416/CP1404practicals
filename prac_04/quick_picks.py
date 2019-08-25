import random


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    # generate random number
    # check if number is in list
    # if number is not in list choose another
    # check again
    # if not in list, append to list
    numbers = []
    for i in range(6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
        numbers.sort()
    return numbers


def print_quick_pick(numbers):
    [print("{:>2}".format(number), end=' ') for number in numbers]
    print("")


main()
