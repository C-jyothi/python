from abc import ABC, abstractmethod

# Abstract class
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass


# Admin subclass
class Admin(User):
    def get_role(self):
        return "Admin"

    # Magic method
    def __str__(self):
        return f"{self.name} is an Admin user."


# Guest subclass
class Guest(User):
    def get_role(self):
        return "Guest"

    # Magic method
    def __str__(self):
        return f"{self.name} is a Guest user."


# Creating objects
admin1 = Admin("Alice", 2020)
guest1 = Guest("Bob", 2023)

# Printing details
print("Role:", admin1.get_role())
print("Account Age:", admin1.account_age(), "years")
print(admin1)

print()

print("Role:", guest1.get_role())
print("Account Age:", guest1.account_age(), "years")
print(guest1)