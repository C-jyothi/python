class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)


# Creating objects
person = Person("Rahul", 30)
employee = Employee("Anjali", 28, "EMP101")
part_time = PartTime("Vivek", 22, 5.5)
consultant = Consultant("Priya", 35, "EMP202", 6.0, "AI Development")

# Displaying details
print("Person Details")
person.show_details()

print("\nEmployee Details")
employee.show_details()

print("\nPart-Time Employee Details")
part_time.show_details()

print("\nConsultant Details")
consultant.show_details()