lst=[1,2,3,4,6,7]#values=6(4,2)

sum=6
for i in lst:
    for j in lst:
        csum=i+j
        if(sum==csum):
            print((i,j))
            break