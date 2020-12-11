f=open("wordcount","r")

dict={}
for lines in f:
#Luminar Technolab - ISO 9001: 2015 Certified Institution
    words=lines.rstrip(",\n").split(" ")
    # print(words)
    # break
#o/p:list=['Luminar', 'Technolab', '-', 'ISO', '9001:2015', 'Certified', 'Institution', '-', 'Software', 'Training', 'Institute.']
    for word in words:
         if word not in dict:
             dict[word]=1
         else:
             dict[word]+=1
for k,v in dict.items():
    print(k,v)
highest=max(dict,key=dict.get)
print(highest)
#calc count
print(highest,dict[highest])