employees=[[1001,"ajay","qa",15000],
          [1002,"vijay","developer",25000],
          [1003,"arun","ba",15000],
          [1004,"amal","developer",30000]]
#print all employee id
for employee in employees:
    print(employee[1])

#find total salary
totalsalary=0
for employee in employees:
    totalsalary+= employee[3]
print(totalsalary)
#find howmany members working as developer
cnt=0
for employee in employees:
    if employee[2]=="developer":
        cnt+=1
print(cnt)
#find total salary group
totalsaldev=totalsalba=totalsalqa=0
for employee in employees:
    if employee[2]=="qa":