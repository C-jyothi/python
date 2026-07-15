# Step 1: Create lists for each workshop
web_development = ["Rahul", "Neha", "Asha"]
data_science = ["Arun", "Meera", "Riya"]
ui_ux_design = ["Kiran", "Sneha", "Anu"]

# Step 2: Combine all lists into a nested list
all_participants = [web_development, data_science, ui_ux_design]

# Step 3: Add a new participant to the Web Development workshop
web_development.append("Vishnu")

# Step 4: Insert a participant at the 2nd position in the Data Science list
data_science.insert(1, "Priya")

# Step 5: Remove the last participant from the UI/UX Design list
ui_ux_design.pop()

# Step 6: Copy the Data Science list and clear the original
copied_data_science = data_science.copy()
data_science.clear()

# Step 7: Display only the first two Web Development participants
print("First two Web Development participants:", web_development[:2])

# Step 8: Create a list of the length of each name in the copied Data Science list
name_lengths = [len(name) for name in copied_data_science]
print("Lengths of Data Science participant names:", name_lengths)

# Step 9: Check if "Asha" is in any workshop list
is_asha_present = (
    "Asha" in web_development or
    "Asha" in data_science or
    "Asha" in ui_ux_design
)
print("Is Asha in any workshop?", is_asha_present)

# Step 10: Create a tuple of the first participant from each workshop list
# (Since data_science is cleared, use the copied list)
first_participants = (
    web_development[0],
    copied_data_science[0],
    ui_ux_design[0]
)
print("First participants tuple:", first_participants)

# Display all lists
print("\nWeb Development:", web_development)
print("Data Science (Original):", data_science)
print("Copied Data Science:", copied_data_science)
print("UI/UX Design:", ui_ux_design)
print("All Participants:", all_participants)