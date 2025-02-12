#write a pogram to find maximum of 3 numbers
def max_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1," is greater")
    elif num2>num1 and num2>num3:
        print(num2," is greater")
    elif num3>num1 and num3>num2:
        print(num3, " is greater")

num1=int(input("Enter number: "))   
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
max_num(num1,num2,num3)