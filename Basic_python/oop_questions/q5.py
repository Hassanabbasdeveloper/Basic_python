# Create Student class
class Student:

    # Class variable (shared by all students)
    school_name = "Future Academy"

    # Constructor
    def __init__(self, name, roll_number):

        # Instance variable
        self.name = name

        # Instance variable
        self.roll_number = roll_number


# Create first object
student1 = Student("Ali", 101)

# Create second object
student2 = Student("Ahmed", 102)

# Print first student's information
print(student1.name)
print(student1.roll_number)
print(student1.school_name)

print()

# Print second student's information
print(student2.name)
print(student2.roll_number)
print(student2.school_name)