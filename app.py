import os
#import logging

from employee import Employee
from register import Register as reg

# Changing the directory
emp_data_folder = os.path.join(os.getcwd(), "employee_data")
os.chdir(emp_data_folder)

# Create employee
new_employee_1 = Employee("Suyash", "Purwar", 16)
new_employee_2 = Employee("Shubham", "Purwar", 21)
new_employee_3 = Employee("Rashi", "Purwar", 15)

reg.register(new_employee_3)
reg.register(new_employee_3)