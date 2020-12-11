f=open("complete.csv")
# for lines in f:
#      print(lines)
#      break
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state] =confirmed_cases
for k,v in dict.items():
    print(k,v)
# highest=max(dict,dict[highest])
# print(highest,dict[highest])
# lowest=min(dict,dict[lowest])
# print(lowest,dict[lowest])
# srt=sorted(dict,key=dict.get,reverse=true)
# print("sorted",srt)8