num1=int(input("number1"))
num2=int(input("number2"))
num3=int(input("number3"))


if((num1>num2)&(num1>num3)):
        print("num1 greater")
elif((num2>num1)&(num2>num3)):
        print("num2 greater")
elif((num3>num1)&(num3>num2)):
        print("num3 greater")
else:
    print("eqal number")