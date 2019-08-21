"""Shortcut key ctrl-alt-l for formatting"""

x = int(input("Enter lower value: "))
y = int(input("Enter upper value: "))
if x % 2 == 1:
    xe = x + 1
else:
    xe = x

if x % 2 == 0:
    xo = x + 1
else:
    xo = x

MENU = """(E)ven numbers in range
(O)dd numbers in range
(S)quare of values in range
(F)inish
"""

print(MENU)
choice = input(">>> ").upper()
while choice != "F":
    if choice == "E":
        # display even numbers
        for i in range(xe, y + 1, 2):
            print(i)
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == "O":
        # display odd numbers
        for i in range(xo, y + 1, 2):
            print(i)
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == "S":
        # Display squares
        for i in range(x, y + 1, 1):
            print(i * i)
        print(MENU)
        choice = input(">>> ").upper()
    else:
        # display invalid message
        print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
print("Finished")
