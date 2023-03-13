# Plan:
# Initialize the number of rabbits to 2
# Initialize the generation counter to 1
# Initialize the total number of rabbits born to 2
# Use a while loop to simulate rabbit breeding until the total number of rabbits exceeds 100
# In each iteration of the loop, double the number of rabbits and increment the generation counter
# Print a message stating the generation at which the total number of rabbits exceeds 100

# Initialize the number of rabbits to 2
generation = 1  
# Initialize the generation counter to 1
rabbits_number = 2 
# Use a while loop to simulate rabbit breeding until the total number of rabbits exceeds 100
while rabbits_number <= 100:
# In each iteration of the loop, double the number of rabbits
	rabbits_number *= 2
# Increment the generation counter
	generation += 1
# Print a message stating the generation at which the total number of rabbits exceeds 100
print ("at generation",str(generation),"over 100 rabits have been born")
