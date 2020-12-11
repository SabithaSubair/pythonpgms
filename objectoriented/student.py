class Student:
    #attribute of person self.name,self.age,self.gender

    def set_student(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def print_student(self):
        print("rol", self.rol)
        print("name",self.name)
        print("course", self.course)
        print("total", self.total)
#reference_name=class()
obj=Student()
obj.set_student(100,"ajay","bca",300)
obj.print_student()