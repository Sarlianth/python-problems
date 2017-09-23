# the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:
# z_next = z - ((z*z - x) / (2 * z))
# Author: Adrian Sypos
# Date: 23/09/2017

import math

x = 20.0

z_next = lambda z: (z - ((z*z - x) / (2 * z)))

current = 1.0

while current != z_next(current):
	current = z_next(current)
	
print('Square root evaluated using Newtons method: ', current)
print('Square root evaluated using math library: ', math.sqrt(x))