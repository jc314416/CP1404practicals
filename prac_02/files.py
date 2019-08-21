# Part 1
user_name = str(input("Enter name: "))
out_file = open("name.txt", 'w')
print("{}".format(user_name), file=out_file)
out_file.close()

# Part 2
in_file = open("name.txt", 'r')
file_read = in_file.read()
print("Your name is {}".format(file_read))
in_file.close()

# Part 3
in_file = open("numbers.txt", 'r')
total = 0
for i in range(2):
    value_read = int(in_file.readline())
    total += value_read
print("{}".format(total))
in_file.close()

# Part 4
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    value_read = int(line)
    total += value_read
print("{}".format(total))
in_file.close()
