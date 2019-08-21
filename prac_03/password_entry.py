"""Russell"""


def main():
    minimum_password_length = 7
    password = get_password(minimum_password_length)

    print_asterisks(password)


def get_password(minimum_password_length):
    password = input("Enter password: ")
    while len(password) < minimum_password_length:
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


main()
