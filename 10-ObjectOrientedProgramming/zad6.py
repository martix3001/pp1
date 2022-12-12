class University:
    # object constructor (__init__ method)
    def __init__(self,name,nr_of_students):
        # object attributes (object features)
        self.name = name 
        self.nr_of_students = nr_of_students    

    
    # object methods (object behaviors)
    def print_name(self):  
        print(self.name)
    def set_name(self, name):
        self.name = name
    def nr_dean_grup(self):
        self.nr_of_grups = self.nr_of_students / 24
        return self.nr_of_grups



u1 = University("UEK",2134124)
u1.print_name()
u1.set_name("UP")
u1.print_name()
print(u1.nr_dean_grup) # naprawictokiedys
