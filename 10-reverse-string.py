# Function to reverse a string.
# Author: Adrian Sypos
# Date: 23/09/2017

# Define a function called reverse accepting a paramenter of a type string
def reverse(string): 
	# String to hold the reversed string
    tmp = reversed(string)
	# Return the reversed string, using join to force evaluate the iterator
    return ''.join(tmp)

# Ask user for a string
print("Enter a string you wish to reverse: ")
# Read in the string into a variable
str = input()
# Print reversed string
print (reverse(str))