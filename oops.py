# Base class Employee
class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.employee_id}, Department: {self.department.name}"

# Subclass Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, name, employee_id, department, team_size):
        # Calling the constructor of the base class
        super().__init__(name, employee_id, department)
        self.team_size = team_size

    # Overriding the get_details method
    def get_details(self):
        return f"Manager Name: {self.name}, ID: {self.employee_id}, Department: {self.department.name}, Team Size: {self.team_size}"

class Department:
    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self

    def get_employee_list(self):
        return [employee.get_details() for employee in self.employees]

# Example usage
if __name__ == "__main__":
    # Create departments
    dept_sales = Department("Sales", 101)
    dept_hr = Department("HR", 102)

    # Create employees and managers
    emp1 = Employee("Alice", "E001", dept_sales)
    emp2 = Employee("Bob", "E002", dept_sales)
    mgr1 = Manager("Charlie", "M001", dept_hr, team_size=5)

    # Add employees to departments
    dept_sales.add_employee(emp1)
    dept_sales.add_employee(emp2)
    dept_hr.add_employee(mgr1)

    # Get employee details
    print(emp1.get_details())  
    print(emp2.get_details())  
    print(mgr1.get_details())  

    # Get list of employees in a department
    print("Employees in Sales Department:")
    print(dept_sales.get_employee_list())

    print("Employees in HR Department:")
    print(dept_hr.get_employee_list())
