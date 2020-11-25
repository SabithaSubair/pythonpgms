lst=["java","python","c#","javascript"]
#print(type(list))
print(lst)
print(lst[0])
print(lst[3])
print(lst[-1])
print(lst[-2])
print(lst[1:3])
#last to first print
print(lst[-1:-5:-1])
#[low:upper:step]
print(lst[0:4:2])
#iteration
for item in lst:
    print(item)
#adding new element
lst.append("dart")
print(lst)
#replace java to ruby
lst[0]="Ruby"
print(lst)
#insert an object into a specific position
lst.insert(3,"perl")
print(lst)