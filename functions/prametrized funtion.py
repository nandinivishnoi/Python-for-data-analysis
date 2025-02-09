#one way
def sub(a,b):
    print(a-b)
    
sub(40,78)

#also we can add return 
def subs(a,b):
    return a-b

print(subs(40,20))

#or if we want the user to give the number
def mul(a,b):
    return a*b

n1=int(input("Enter your number: "))
n2=int(input("Enter your another number: "))

print(mul(n1,n2))
