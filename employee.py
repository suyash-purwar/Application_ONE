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
        return {
            "name": self.get_name(),
            "age": self.age,
            ''' 
                id property is not defined by the init function
                This property will be added when the employee object
                will be registered.
                Register class is responsible for this action
            '''
            "id": self.id
        }
        
    ''' Returns the formated full name of the employee '''    
    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)