# Guessing game. User must guess a random generated number between 1 and 20. After each attempt program let's user know if the number he tried is too high or too low. Counts the number of tries as well.
# Author: Adrian Sypos
# Date: 22/09/2017

# This is a guess the number game.
import random
guessesTaken = 1

number = random.randint(1, 20)

print('Try to guess a number between 1 and 20')
guess = input()
guess = int(guess)
if guess < number:
	print('Your guess is too low.')

if guess > number:
	print('Your guess is too high.')

while guess != number:
	print('Try again.')
	guess = input()
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
		print('Your guess is too low.')

	if guess > number:
		print('Your guess is too high.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Good job! You guessed the number in ' + guessesTaken + ' guesses!')