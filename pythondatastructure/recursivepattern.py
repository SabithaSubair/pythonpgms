patterns=["a","b","a","b","a"]

cnt=0
for pattern in patterns:
    if pattern=="a":
        cnt+=1
        break

    elif pattern=="b":
        cnt += 1
print("a",cnt)
print("b",cnt)