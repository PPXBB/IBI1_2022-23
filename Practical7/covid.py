# Importing necessary libraries for working with data, visualizing data, and performing mathematical operations.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Changing the current working directory to the folder where the data is located,
# reading the data into a Pandas dataframe, and using some basic Pandas functions to get a sense of the data.
os.chdir("D:\pycode\data")
covid_data = pd.read_csv("full_data.csv")
covid_data.head()
covid_data.info()
covid_data.describe()
# Using Pandas' iloc[] method to subset the data by selecting every 100th row for the second column.
covid_data.iloc[0:1000:100,1]
covid_data.loc[0:81,"total_cases"]
# Creating a boolean list for the location "Afghanistan" using a for loop, and
# then using the boolean list to extract the total cases for Afghanistan using Pandas' loc[] method.
Afghanistan = []
location = covid_data.loc[:,"location"]
for i in location:
    if i=="Afghanistan":
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
covid_data.loc[Afghanistan,"total_cases"]
# Creating boolean lists for locations that are not "World" and locations that are "World",
# and then using the boolean lists to create new dataframes for country data and world data.
country = []
for i in location:
    if i=="World":
        country.append(False)
    else:
        country.append(True)
world = [not i for i in country]
country_data = covid_data.loc[country,:]
world_data = covid_data.loc[world,:]
# Creating a boolean list for the date "2020-03-31" and then
# using it to extract data from the country data for March 31, 2020 and assigning it to new_data.
March_31_2020 = []
date = country_data.loc[:,"date"]
for i in date:
    if i=="2020-03-31":
        March_31_2020.append(True)
    else:
        March_31_2020.append(False)
new_data = country_data.loc[March_31_2020,:]
# Calculating the mean of new cases and new deaths using NumPy's mean() function
# and printing the values to the console.
mean_cases = np.mean(new_data.loc[:,"new_cases"])
print(mean_cases)
mean_deaths = np.mean(new_data.loc[:,"new_deaths"])
print(mean_deaths)
# Creating box plots using Matplotlib's boxplot() function to visualize the distribution of new cases
# and new deaths for different countries on March 31, 2020.
plt.boxplot(new_data.loc[:,"new_cases"])
plt.title("new cases of different countries on 31 March 2020")
plt.show()
plt.boxplot(new_data.loc[:,"new_deaths"])
plt.title("new deaths of different countries on 31 March 2020")
plt.show()
# Creating a plot chart that shows the new cases and new deaths across the world over time.
world_dates = world_data.loc[:,"date"]
world_new_cases = world_data.loc[:,"new_cases"]
world_new_deaths = world_data.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_cases, 'ro',markersize = '4')
plt.plot(world_dates, world_new_deaths, 'bx',markersize = '4')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title("new cases and new deaths across the world")
plt.show()

# the following is my answer for the question
# Create an empty list to store the names of countries with over 10,000 total cases
country_list = []
# Extract the names of countries with over 10,000 total cases from the new_data dataframe
country_over_10000 = new_data.loc[new_data["total_cases"] > 10000, "location"]
# Create a new figure to display the bar chart of total cases for each country
plt.figure(figsize=(9,4), dpi=200)
# Create a bar chart of the total cases for each country
plt.bar(new_data["location"], new_data["total_cases"])
# Set the x-ticks to be the names of countries with over 10,000 total cases
plt.xticks(country_over_10000, rotation=-80, size=10)
# Add a title and labels to the plot
plt.title("total infections")
plt.ylabel("number")
# Display the bar chart
plt.show()
# Add the names of countries with over 10,000 total cases to the country_list
for i in country_over_10000:
    country_list.append(i)
# Print the list of countries with over 10,000 total cases
print("The fowllowing are the countrie with over 10,000 total cases")
print(country_list)
