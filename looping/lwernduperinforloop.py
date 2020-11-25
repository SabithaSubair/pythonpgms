low=int(input("lower limit:"))
uper=int(input("upper limit:"))

for num in range(low,uper+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
    else:
        print(num)