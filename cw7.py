# Initial Grocery List
grocery_list = ["milk", "bread", "eggs"]

# Function to add an item
def add_item(item):
    grocery_list.append(item)

# Function to remove the last item
def remove_last_item():
    if grocery_list:
        grocery_list.pop()
    else:
        print("The grocery list is empty.")

# Lambda function to display each item
display_item = lambda item: print("Item:", item)

# Recursive function to count total characters
def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])

# Add a new item
add_item("butter")

# Remove the last item
remove_last_item()

# Display the grocery list
print("Grocery List:")
for item in grocery_list:
    display_item(item)

# Count total characters
total = count_characters(grocery_list)
print("Total number of characters:", total)