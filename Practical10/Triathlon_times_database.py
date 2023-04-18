# Define the Triathlon class
class triathlon:
    # Initialize attributes in the constructor
    def __init__(self, first, last, location, swim, cycle, run, total):
        self.first = first       # First name
        self.last = last        # Last name
        self.location = location  # Location of triathlon
        self.swim = swim         # Time for swim leg
        self.cycle = cycle       # Time for cycling leg
        self.run = run           # Time for running leg
        self.total = total       # Total time
    # Method to print details
    def info(self):
        print(f"{self.first} {self.last} ({self.location}): Swim {self.swim} Cycle {self.cycle} Run {self.run} Total {self.total}")
 # Create a Triathlon object for "John Doe"
john = triathlon("John", "Doe", "London", 15, 45, 20, 80)
 # Call the info() method (syntax error)
print(john.info())