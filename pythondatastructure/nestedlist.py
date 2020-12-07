students=[[1001,"ajay","mca",150],
          [1002,"viajay","bca",145],
          [1003,"arun","mca",150],
          [1004,"amal","bca",135]]
#print all student name
for student in students:
    print(student[1])
#print roll number
for student in students:
    print(student[0])
#print all student details whose course='mca'
for student in students:
    if(student[2]=="mca"):
          print(student)
#print all stud total >140
for student in students:
    if (student[3]>140):
            print(student[1])
#prinnt total sum of student total by course
totalmca=0
totalbca=0
for student in students:
    if (student[2]=="mca"):
        totalmca+=student[3]
    elif (student[2]=="bca"):
            totalbca+=student[3]
print("mca total:",totalmca)
print("bca total:",totalbca)
