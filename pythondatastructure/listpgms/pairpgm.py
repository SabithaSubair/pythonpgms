lst=[2,1,3,4,6,7]
lst.sort()
#[1,2,3,4,6,7]
#l          U
#6

#lst[l]+lst[u]==6   (1+7=8)
#if searching element < total:move upper backword
#6<8

#lst[l]+lst[u]==6   (1+6=7)
#6<7

low=0
upp=len(lst)-1
element=int(input("enter element"))
while(low<upp):
    total=lst[low]+lst[upp]
    #case 1
    if(element<total):
        upp=upp-1
        #case 2
    elif(element>total):
        low=low+1
        #case 3
    elif(element==total):
        print("Pairs are",lst[low],",",lst[upp])
        break
