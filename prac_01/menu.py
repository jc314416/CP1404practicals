"""get name"""
name = str(input("Enter name: "))
"""display menu"""
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
"get choice"
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        """display "hello" name"""
        print("Hello {}".format(name))
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == "G":
        """display "goodbye" name"""
        print("Goodbye {}".format(name))
        print(MENU)
        choice = input(">>> ").upper()
    else:
        """display invalid message"""
        print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    """
   display menu
   get choice
display finished message"""
print("Finished")
