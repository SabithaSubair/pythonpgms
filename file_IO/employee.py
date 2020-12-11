f=open("emp","r")
emp_dict={}
for lines in f:
    print(lines)
    #100,don,developer,2,2500
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")

    if id not in emp_dict:
        emp_dict[id]={"id":id,"name":name,"desig":desig,"exp":exp,"salary":salary}
    print(emp_dict)