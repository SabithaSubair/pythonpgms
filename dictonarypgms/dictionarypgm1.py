#values of dictionary in the form of keyvalue pairs
students={"roll":100,"name":"ajay","course":"mca"}
print(students["roll"])
print(students["name"])
print(students["course"])
for key in students:
    print(key,students[key])
#another method
for k,v in students.items():
    print(k,v)
#checking for specific key
print("roll" in students)
#checking for total key
print("total" in students)
#add total
if("total" not in students):
    students["total"]=150
    print(students)
#add total value 50
students["total"]+=50
print(students)

