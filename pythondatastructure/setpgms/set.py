st=set()
print(type(st))
stt={1,2,3,4}
sttt={5,6,7}
print(stt)
print(sttt)

#indexing not supported in set... ie st[0] not
#update
stt.update(sttt)
print(stt)
#union
unionset=stt.union(sttt)
print(unionset)