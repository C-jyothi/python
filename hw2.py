# Multiline string
paragraph = """
Python is a powerful programming language.
This course teaches Python basics, data types,
loops, functions, and object-oriented programming.
"""

# Display the length of the paragraph
print("Length of paragraph:", len(paragraph))

# Display the first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Print the first 50 characters
print("Preview:", paragraph[:50])

# Replace "Python" with "PYTHON"
new_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter Replace:")
print(new_paragraph)

# Convert to lowercase
print("\nLowercase:")
print(paragraph.lower())

# Remove extra spaces from the beginning and end
trimmed = paragraph.strip()
print("\nAfter strip():")
print(trimmed)

# Split into words
words = trimmed.split()
print("\nWords List:")
print(words)

# Check if "course" exists
if "course" in trimmed:
    print("\nThe word 'course' is found.")
else:
    print("\nThe word 'course' is not found.")

# Final message using format()
print("\nThe course description is {} characters long and has {} words."
      .format(len(trimmed), len(words)))