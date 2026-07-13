import random

# Store the volume of each juice
apple = 15.5
orange = 20
grape = 10.25

# Calculate the total volume
total = apple + orange + grape

# Print the total volume
print("Total volume:", total)

# Convert the total volume to an integer
total_int = int(total)
print("Integer value:", total_int)

# Convert the total volume to a string
total_str = str(total)
print("Total volume as string: " + total_str + " liters")

# Generate a random number between 5 and 10
bonus = random.randint(5, 10)

# Add the bonus liters to the total
final_total = total + bonus

# Print the final total
print("Bonus liters:", bonus)
print("Final total volume:", final_total)