#low=int(input("enter the low limit"))
#up=int(input("enter the upper limit"))
#evsum=0
#odsum=0
#for i in range(low,up):
  #  if(i%2==0):
   #     evsum=


   #prime no
   #7...1,7...prime
   #inn caseof 7....1,7 exclude
num=int(input("enter num"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
        #factor
    else:
        flag=0
        #not factor
if(flag==0):
    print("prime num")
else:
    print("not prime")