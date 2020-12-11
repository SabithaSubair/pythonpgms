f=open("complete.csv","r")
covid_data={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    cured=data[6]
    death=data[5]
    confirmed=data[4]
    if state not in covid_data:
        covid_data[state]={
            "state":state,
            "confirmed":confirmed,
            "cured":cured,
            "death":death
        }
    else:
        covid_data[state] = {
            "state": state,
            "confirmed": confirmed,
            "cured": cured,
            "death": death
        }

 #print gdetails
# i=0
# for k,v in covid_data.items():
#     if i==5:
#         break

#     print(k,v)

print("display purticular state confirmed case details")
def print_covid_data(**kwargs):
    state=kwargs.get("state")
    if state in covid_data:
        print(state,covid_data[state]["confirmed"])
        if "property" in kwargs:
            prop=kwargs["property"]
            if prop in covid_data[state]:
                print(covid_data[state][prop])
    else:
        print("not privided name")
print_covid_data(state="Kerala",property="death")





