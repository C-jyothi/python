# Step 1
has_account = True

# Step 2
email_verified = False

# Step 3
can_login = has_account and email_verified

# Step 4
email = "g@example.com"
is_email_valid = "@" in email

# Step 5
user_age = 17
is_age_valid = user_age >= 18

# Step 6
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

# Step 7
print("Can Login:", can_login)
print("Is Email Valid:", is_email_valid)
print("Is Age Valid:", is_age_valid)
print("Can Login Final:", can_login_final)

# Step 8
print("Has Account is True:", has_account is True)