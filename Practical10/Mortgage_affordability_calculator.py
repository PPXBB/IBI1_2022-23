def can_afford_house(value, salary):
    """Determines if a house is affordable based on salary."""
    # If the house value is less than or equal to 5 times the salary,
    # the house is affordable
    if value <= 5 * salary:
        return "Yes"
    # Otherwise, the house is not affordable
    else:
        return "No"

# Set the house value and purchaser's annual salary
house_value = 350000
purchaser_salary = 40000
# Call the function and pass the house value and salary
can_afford = can_afford_house(house_value, purchaser_salary)
# Print the result
print(can_afford)