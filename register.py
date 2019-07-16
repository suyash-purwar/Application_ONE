import csv

class Register:
    initial_id = 0
    
    @classmethod 
    def assign_id(cls, emp):
        cls.initial_id += 1
        emp.id = cls.initial_id

    
    @classmethod
    def doesExist(cls, employee):
        if employee.hasID() == False:
            print("Haan")
            cls.assign_id(employee)
        
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
        
    @classmethod
    def register(cls, employee):
        if employee.hasID() == False:
           cls.assign_id(employee)
            
        fieldname = ["name", "age", "id"]
        
        if employee.id == 1:
            with open("employee.csv", "w", newline="") as emp_csv:
                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname, delimiter=",")
        
        if(cls.doesContainHeader() == False):
            with open("employee.csv", "w", newline="") as emp_csv:
                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname, delimiter=",")
                csv_writer.writeheader()
                csv_writer.writerow(employee.get_info())
            print("Doesn't contain Header")
            print("Employee is registered")
        else:
            if (cls.doesExist(employee) == False):
                with open("employee.csv", "a", newline="") as emp_csv:
                    csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname)
                    csv_writer.writerow(employee.get_info())
                print("Employee is registered")
