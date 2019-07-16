import os

from employee import Employee
from register import Register as reg

# Changing the directory
emp_data_folder = os.path.join(os.getcwd(), "employee_data")
os.chdir(emp_data_folder)

# Create employee
emp1 = Employee("Alex", "Raymond", 27)
emp2 = Employee("Maria", "Hirschi", 34)
emp3 = Employee("Henry", "Lamb", 41)


reg.register(emp2)
reg.register(emp3)
reg.register(emp1)
reg.register(Employee("Kelly", "Overton", 42))