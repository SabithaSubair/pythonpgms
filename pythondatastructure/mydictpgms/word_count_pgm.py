text="hello hai hai hai hai hello hello"
#o/p hello:3 hai :4
#print word count
words=text.split(" ")
#print(words)
dict={}
#dict[word]=1##hello id that word not in dict
#dict[word]+=1 #if that word not in dictionary
for word in words:#"hello" 1st check then hai etc
     if(word not in dict):
         dict[word]=1
     else:
         dict[word]+=1
print(dict)
