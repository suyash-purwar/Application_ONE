'''
    Sole purpose of this class is to create employee objects
    
    These objects will be passed on the Register Class's registry method
    
    Register().register(Employee(first_name, last_name, age)) is responsible for saving employee's data
    in the CSV file
    
    Regisrer class is responsible for adding 'id' property in the employee object
'''
    
    

class Employee():
    company = "Aeologic Technologies"
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    ''' Checks whether the employee has id property or not '''
    def hasID(self):
        try:
            if self.id:
                return True
        except:
            return False
    
    ''' Returns the name of the organization '''
    @classmethod
    def get_org(cls):
        return cls.company
        
    ''' Returns the information of the employee in the form of a dictionary '''
    def get_info(self):
        ''' 
            id property is not defined by the init function
            This property will be added when the employee object
            will be registered.
            Register class is responsible for this action
        '''
        return {
            "name": self.get_name(),
            "age": self.age,
            "id": self.id
        }
        
    ''' Returns the formated full name of the employee '''    
    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)