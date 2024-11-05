import boto3
from botocore.exceptions import NoCredentialsError

# DynamoDB connection setup for region 'ap-south-1'
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('organization')

# Parent class: Department
class Department: # super class
    def __init__(self, dept_name):
        self._dept_name = dept_name  # Encapsulation (data hiding)

    def get_dept_name(self):
        return self._dept_name

    # Method to save department details in DynamoDB
    def save_department(self):
        try:
            table.put_item(
                Item={
                    'PK': f'DEP#{self._dept_name}',
                    'SK': f'DEPT',
                    'Name': self._dept_name,
                    'Role': 'Department'
                }
            )
            print(f"Department '{self._dept_name}' saved successfully.")
        except NoCredentialsError:
            print("Credentials not available.")

# Child class: Employee inherits Department (Inheritance)
class Employee(Department):
    def __init__(self, emp_name, emp_role, dept_name):
        super().__init__(dept_name)  # Calling the parent class constructor
        self.__emp_name = emp_name  # Encapsulation
        self.__emp_role = emp_role  # Encapsulation

    # Polymorphism: Overriding save method to save employee details
    def save_employee(self):
        try:
            table.put_item(
                Item={
                    'PK': f'EMP#{self.__emp_name}',
                    'SK': f'EMP#{self.get_dept_name()}',
                    'Name': self.__emp_name,
                    'Role': self.__emp_role,
                    'DepartmentName': self.get_dept_name()
                }
            )
            print(f"Employee '{self.__emp_name}' saved successfully in department '{self.get_dept_name()}'.")
        except NoCredentialsError:
            print("Credentials not available.")

# Example Usage

# Creating a department
dept_hr = Department("Human Resources")
dept_hr.save_department()

# Creating employees in that department
emp1 = Employee("Amit Sharma", "Manager", dept_hr.get_dept_name())
emp2 = Employee("Suman Rao", "Assistant Manager", dept_hr.get_dept_name())

# Saving employees
emp1.save_employee()
emp2.save_employee()

# Polymorphism example: saving department and employees using a common method
def save_entity(entity):
    if isinstance(entity, Department):
        entity.save_department()
    elif isinstance(entity, Employee):
        entity.save_employee()

# Creating a new department and employee to demonstrate polymorphism
dept_it = Department("Information Technology")
emp3 = Employee("Ravi Kumar", "Software Engineer", dept_it.get_dept_name())

# Saving using polymorphism
save_entity(dept_it)
save_entity(emp3)
