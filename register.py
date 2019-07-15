import csv

class Register:
    @staticmethod
    def doesExist(employee):
        with open("employee.csv", "r") as emp_csv:
            csv_reader = csv.DictReader(emp_csv)
            
            for line in csv_reader:
                if int(line["id"]) == employee.id:
                    return True
                
        return False
        
    @staticmethod
    def doesContainHeader():
        with open("employee.csv") as emp_csv: 
            read = csv.DictReader(emp_csv)
            
            for line in read:
                return True
            
            return False
            
#    @classmethod
#    def register(cls, employee):
#        if (cls.doesExist(employee) != True):
#            with open("employee.csv", "a", newline="") as emp_csv:
#                fieldName = ["name", "age"]
#                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldName, delimiter=",")
#                csv_writer.writerow(employee.get_info())
#            print("Employee is registered")
#        else: 
#            print("Employee is already registered")
            
    @classmethod
    def register(cls, employee):
        fieldname = ["name", "age", "id"]
        if(cls.doesContainHeader() == False):
            print("Noooooooooooooooooooooooooo")
            with open("employee.csv", "w", newline="") as emp_csv:
                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname, delimiter=",")
                csv_writer.writeheader()
                csv_writer.writerow(employee.get_info())
            print("Doesn't contain Header")
            print("Employee is registered")
        else:
            print("yesssssssssssssssssss")
            if (cls.doesExist(employee) == False):
                with open("employee.csv", "a", newline="") as emp_csv:
                    csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname)
                    csv_writer.writerow(employee.get_info())
                print("Employee is registered")
