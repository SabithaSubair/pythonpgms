#in=123..o/p=321
n1=int(input("Enter the number:"))
res=0
while(n1!=0):
    digit=n1%10
    res=res*10+digit
    n1=n1//10
print(res)