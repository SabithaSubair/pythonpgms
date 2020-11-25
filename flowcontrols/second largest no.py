num1=int(input("number1"))
num2=int(input("number2"))
num3=int(input("number3"))


if((num1>num2)^(num1>num3)):
        print(" 2nd greater number is:",num1)
elif((num2>num1)^(num2>num3)):
        print("2nd greater number is:",num2)
elif((num3>num2)^(num1<num3)):
        print(" 2nd greater number is:",num3)
else:
    print("eqal numbers",num1)