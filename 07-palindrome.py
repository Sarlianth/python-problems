# Function that tests whether a string is a palindrome
# Author: Adrian Sypos
# Date: 23/09/2017

# Ask user to input a string
print("Please enter a word to check for palindrome: ")
# Read in the string
word = input()
# Bring the string to lower case for obvious comparison reasons
word = word.casefold()
# Logical statement to check if the string is equal to the same string reversed
if(word == word[::-1]):
	print("This word is a palindrome!")
# If it's not a palindrome..
else:
	print("Sorry, this word isn't a palindrome..")