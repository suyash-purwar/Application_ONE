import csv

class Register:
    initial_id = 0
    
    @classmethod 
    def assign_id(cls, emp):
        cls.initial_id += 1
        emp.id = cls.initial_id
        
    @staticmethod
    def countEmployees():
        emp_count = 0
        with open("employee.csv", "r", newline="") as emp_csv:
            csv_reader = csv.DictReader(emp_csv)
            
            for emp_index in csv_reader:
                emp_count += 1
                
            return emp_count
            
    
    @classmethod
    def doesExist(cls, emp):
        if not emp.hasID():
            cls.assign_id(emp)
        
        with open("employee.csv", "r") as emp_csv:
            csv_reader = csv.DictReader(emp_csv)
            
            for line in csv_reader:
                if int(line["id"]) == emp.id:
                    return True
                
        return False
        
    @staticmethod
    def doesContainHeader():
        with open("employee.csv") as emp_csv: 
            read = csv.DictReader(emp_csv)

            for line in read: return True

            return False
        
    @classmethod
    def register(cls, emp):
        fieldname = ["name", "age", "id"]

        if not emp.hasID(): cls.assign_id(emp)
        
        if emp.id == 1:
            with open("employee.csv", "w", newline="") as emp_csv:
                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname, delimiter=",")
        
        if(cls.doesContainHeader() == False):
            with open("employee.csv", "w", newline="") as emp_csv:
                csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname, delimiter=",")
                csv_writer.writeheader()
                csv_writer.writerow(emp.get_info())

        else:
            if (cls.doesExist(emp) == False):
                with open("employee.csv", "a", newline="") as emp_csv:
                    csv_writer = csv.DictWriter(emp_csv, fieldnames=fieldname)
                    csv_writer.writerow(emp.get_info())
