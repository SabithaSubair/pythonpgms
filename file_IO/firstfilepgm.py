#file operations READ WRITE APPEND
#step 1 Create reference
#reference_name=open(filepath,mode_of_operation)

f=open("names","r")
# for lines in f:
#     print(lines)
# #print using list
# print("using  list")
lst=[]
for lines in f:
    lst.append(lines)
print(lst)
#remove slash  from o/p
data="hello\n"
data=data.rstrip("\n")
print(data)
#so final o/p is:
# lst=[]
# for lines in f:
#     lst.append(lines.rstrip("\n"))
# print(lst)