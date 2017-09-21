# Function that calculates the sum of the digits of the factorial of a number. Find the sum of the digits in the number 100!
# Author: Adrian Sypos
# Date: 21/09/2017

# Imports
import math

# Print the factorial of 100!
print (math.factorial(100))

# Assign the 100! to a variable
n = math.factorial(100)

# Create a list of integers
# List is populated from a string that contains the long number from 100!
numbers = [int(d) for d in str(n)]

# Print the list to see if it works
print(numbers)

# Print the sum of the digits in the number 100!
print(sum(numbers))