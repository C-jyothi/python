# Multiline string for the receipt header
header = """******** BOOK STORE ********
Customer Receipt
----------------------------
"""

# Book details
book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

# Receipt lines using {} placeholders and format()
line1 = "Book:\t{}\tPrice: ₹{}\n".format(book1, price1)
line2 = "Book:\t{}\tPrice: ₹{}\n".format(book2, price2)

# Calculate total
total = price1 + price2
total_line = "Total:\t₹{}\n".format(total)

# Thank-you message
message = "Thank you for shopping with us!"

# Concatenate all parts
receipt = header + line1 + line2 + total_line + message

# Display the receipt in uppercase
print(receipt.upper())