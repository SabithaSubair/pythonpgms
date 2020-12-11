#class---design pattern,plan,template,blueprint

#object---real world entity

#reference
#create class using "class"
#class classname
class Person:
    #attribute of person self.name,self.age,self.gender

    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_person(self):
        print("name",self.name)
        print("age", self.age)
        print("gender", self.gender)
#reference_name=class()
obj=Person()
obj.set_person("ajay",20,"male")
obj.print_person()