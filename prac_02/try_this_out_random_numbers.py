import random

print(random.randint(5, 20))
# Returned a 7, would expect a random number from 5 to 19

print(random.randrange(3, 10, 2))
# Returned a 7, would expect and odd number from 3 to 9

print(random.uniform(2.5, 5.5))
# Returned 3.5488459477637466, would expect number in range 2.5 to
# <5.5 depending on rounding, floating point value
