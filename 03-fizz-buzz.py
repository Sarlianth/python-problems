# Fizz buzz program in python. The objective for this program is to  prints the numbers from 1 to 100, except for the following conditions; for multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
# Author: Adrian Sypos
# Date: 21/09/2017

# For loop from 1 - 100 
for num in range(1,101):
	# If the number which multiples are both three and five, print FizzBuzz
    if num % 5 == 0 and num % 3 == 0:
        print ("FizzBuzz")
    # For multiples of three
	elif num % 3 == 0:
        print ("Fizz")
    # For multiples of five
	elif num % 5 == 0:
        print ("Buzz")
    # For the rest of the numbers
	else:
        print (num)