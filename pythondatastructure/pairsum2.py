lst=[2,5,6,3]#[14,11,10,13]
#lst=[4,3,2,5]#[10,11,12,9]
total=sum(lst)#16
out=[]
for num in lst:#5,6,3
    out.append((total-num))#16-2=4,16-5=11
print(out)
