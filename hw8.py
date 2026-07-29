
# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


# Derived class Trainer
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


# Derived class YogaInstructor
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


# Multiple Inheritance
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


# Creating objects
emp = Employee("Rahul", "Receptionist")
trainer = Trainer("Anita", "Trainer", "Weight Training")
yoga = YogaInstructor("Sneha", "Yoga Instructor", "Hatha Yoga")
multi = MultiTrainer("Arjun", "Multi Trainer", "CrossFit", "Vinyasa Yoga")

# Displaying details
print("Employee Details")
emp.display()

print("\nTrainer Details")
trainer.display()

print("\nYoga Instructor Details")
yoga.display()

print("\nMultiTrainer Details")
multi.display()