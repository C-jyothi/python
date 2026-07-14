# Step 1
is_logged_in = True
is_subscribed = False

# Step 2
user_credits = 100
max_credits = 200
min_credits = 50

# Step 3
credits_valid = (user_credits >= min_credits and
                 user_credits <= max_credits and
                 user_credits != min_credits)

# Step 4
bonus_eligible = is_subscribed or (not (user_credits <= min_credits))

# Step 5
user_credits += 50   # 150
user_credits -= 20   # 130
user_credits *= 2    # 260
user_credits %= 150  # 110

# Step 6
power_result = user_credits ** 2

# Step 7
full_access = is_logged_in and is_subscribed

# Step 8
is_true_login = (is_logged_in is True)

# Step 9
access_result = is_logged_in or is_subscribed and False

# Step 10
print("Is Logged In:", is_logged_in)
print("Is Subscribed:", is_subscribed)
print("Credits Valid:", credits_valid)
print("Bonus Eligible:", bonus_eligible)
print("User Credits:", user_credits)
print("Power Result:", power_result)
print("Full Access:", full_access)
print("Is True Login:", is_true_login)
print("Access Result:", access_result)