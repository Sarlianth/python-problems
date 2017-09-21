# Simple python program to display current date and time.
# Author: Adrian Sypos
# Date: 21/09/2017

# Imports
import time;

# Creating variable localtime that returns a time-tuple with all nine items valid
localtime = time.localtime(time.time())
# Printing localtime unformatted 
print ("Local current time :", localtime)

# Formatting the localtime into readable format
localtime = time.asctime( time.localtime(time.time()))
# Printing formatter time
print ("Local current time :", localtime)