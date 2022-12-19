class Student():
    
    uni_name = "Uniwersytet Ekonomiczny"
    id_count = 100000
    def __init__(self, name,surname,field_of_study):
        self.name = name 
        self.id = id
        self.surname = surname
        self.fiel_of_study = field_of_study
        self.id = Student.id_count
        Student.id_count += 1
       
    def __str__(self):
        self.studentdata = f"{self.name} {self.surname} ,({self.id}) , {self.fiel_of_study},  {Student.uni_name} "
        return self.studentdata

    
student1 = Student("Anna","MAY","ACS")
student2 = Student("Mikolaj","Suchan","TPI")
student2 = Student("Yo","YOYO","TPI")
print(student1)
print(student2)

