# Function that returns the largest and smallest elements in a list.
# Author: Adrian Sypos
# Date: 22/09/2017

# Initialise an empty list
list = []

# Ask user to input the numbers
print("Please enter 10 random numbers into the list")
# Read each number using a for loop
for n in range(10):
    numbers = int(input('Enter number '))
	# Append each number to the list
    list.append(numbers)
# Finally, print the largest and the smallest value from the list
print("Largest: ", max(list), "\nSmallest: ", min(list))