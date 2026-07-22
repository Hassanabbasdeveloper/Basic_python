# Create Employee class
class Employee:

    # Class variable for starting ID
    next_id = 101

    # Constructor
    def __init__(self, name):

        # Store employee name
        self.name = name

        # Assign current ID
        self.employee_id = Employee.next_id

        # Increase ID for next employee
        Employee.next_id += 1


# Create employee objects
emp1 = Employee("Ali")
emp2 = Employee("Ahmed")
emp3 = Employee("Hassan")

# Print employee details
print(emp1.name, emp1.employee_id)
print(emp2.name, emp2.employee_id)
print(emp3.name, emp3.employee_id)