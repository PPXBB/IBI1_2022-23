# What does this piece of code do?
# Answer:This code generates 10 random numbers between 1 and 100 and stores the 
# largest of these numbers, which is then printed to the console.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# The variable progress is used to track how many random numbers have been generated so far,
# and stored_random_number is used to keep track of the largest number seen so far, initialized to zero.
progress=0
stored_random_number=0
# Loop 10 times
while progress<10:
# Increment the progress variable by 1 in each iteration
    progress += 1
# Generate a random integer between 1 and 100 and store it in the n variable
    n = randint(1,100)
# If the current number (n) is greater than the stored random number
    if n > stored_random_number:
        stored_random_number = n
# Print the final stored random number, which is the largest among the 10 random numbers generated.
print(stored_random_number)
