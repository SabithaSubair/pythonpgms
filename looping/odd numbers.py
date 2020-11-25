low=int(input("Enter lower limit: "))
up=int(input("Enter upper limit: "))
#sum of all odd numbers
sum=0
if(low>up):
    print("Error")
while(low<=up):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)
#even==   if(low%2==0):