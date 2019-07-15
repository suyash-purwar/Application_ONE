class Employee():
    company = "Aeologic Technologies"
    initial_id = 0
    
    @classmethod
    def assign_id(cls):
        cls.initial_id += 1
        return cls.initial_id
    
    @classmethod
    def get_org(cls):
        return cls.company
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = self.assign_id()
        
        # TODO: Implement logger
        
    def get_info(self):
        return {
            "name": self.get_name(),
            "age": self.age,
            "id": self.id
        }
        
    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)