# Function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# Author: Adrian Sypos
# Date: 23/09/2017

# Initialize the lists with appropiate values
list = [1, 4, 6]
list2 = [2, 3, 5]

# Print the lists
print('This is my list', list)
print('This is my list2', list2)

# Merge the lists
listMerged = list + list2

# Print the list merged
print('This is merged list', listMerged)
# Print merged list sorted in ascending order
print('Merged and sorted list', sorted(listMerged))
# Print merged list sorted in descending order
print('Merged and sorted in reverse', sorted(listMerged, reverse=True))