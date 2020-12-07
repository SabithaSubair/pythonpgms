#normal method
# def add(num1,num2):
#     res=num1+num2
#     print(res)
# add(10,20)
#variale length argument methods
# def add(*nums):
#     print(nums)#accepted by tuple forms
# add(10,20)
# add(10,20,30)
#calc sum
def add(*args):
     total=0
     for num in args:
         total+=num
     print(total)

add(10,20)
add(10,20,30)

#*args accept in tuple format
def printEmp(**args):
    print(args)
printEmp(home="kakkanad",name="ajay",working="luminar")



