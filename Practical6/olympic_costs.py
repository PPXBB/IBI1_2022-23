# Plan:
# Create two lists: Olmpic_Games and costs.
# Use the zip function to create a dictionary named years_costs by mapping Olmpic_Games to costs.
# Use the sorted function to sort the years_costs dictionary by the values (costs).
# Create a list named sorted_years containing the keys of the sorted dictionary.
# Create a list named sorted_costs containing the sorted values of the costs list.
# Import matplotlib and numpy libraries.
# Create an array of numbers using numpy.arange function and the length of the sorted_costs list.
# Create a bar chart using plt.bar function and pass sorted_costs as data and sorted_years as labels.
# Add a y-axis label using plt.ylabel.
# Add a title using plt.title.
# Use plt.xticks to display the sorted years on the x-axis.


Olmpic_Games=["1984", "1988", "1992", "1996", "2000", "2004", "2008", "2012"]
costs=[1,8,15,7,5,14,43,40]
# Create a dictionary named years_costs by mapping Olmpic_Games to costs.
years_costs=dict(zip(Olmpic_Games,costs))
# Sort the dictionary by the values (costs).
sorted_dict = dict(sorted(years_costs.items(), key=lambda item: item[1]))
# Create lists of sorted years and costs.
sorted_years=sorted_dict.keys()
sorted_costs=sorted(costs)
print(sorted_costs)
import matplotlib.pyplot as plt
import numpy as np
# Create an array of numbers for the x-axis.
number=np.arange(len(sorted_costs))
# Create a bar chart.
plt.bar(number, sorted_costs, color="orange")
# Add labels and title
plt.ylabel("Cost (in $ billions)")
plt.title("the cost of hosting the Summer Olympic Games")
# Display sorted years on the x-axis.
plt.xticks(number,sorted_years)
# Display the chart.
plt.show()


