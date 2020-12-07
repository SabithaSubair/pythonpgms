students={
          100:{"rol":100,"name":"ajay","total":140,"course":"bca"},
          101:{"rol":101,"name":"vijay","total":145,"course":"bca"},
          102:{"rol":102,"name":"vijay","total":145,"course":"bca"},
          103:{"rol":103,"name":"anu","total":130,"course":"bca"},
          104:{"rol":104,"name":"jay","total":135,"course":"mca"},
          }
print(students[100])#print whole dtails
#print only name
print(students[100]["name"])
#print only total
print(students[100]["total"])

def printStudent(**kwargs):#id-101
    id=kwargs.get("id")#100 id=kwargs[id] 101
    if(id in students):
        print(students[id]["name"])
    else:
        print("not exist")
printStudent(id=104)
#if stud not exist
printStudent(id=109)
#only print a purtivcular property
printStudent(id=103,property="total")
#other method
print("other method")
def printStudent(**kwargs):#id-101
    id=kwargs.get("id")#100 id=kwargs[id] 101
    if(id in students):
        if "property" in kwargs:
            prop=kwargs.get("property")#total
            if prop in students[id]:
                 print(students[id][prop])
        print(students[id]["name"])

    else:
        print("not exist")
printStudent(id=104, property="total")