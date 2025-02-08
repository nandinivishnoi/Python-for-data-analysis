#tuple are immutable i.e. they can not be changed once created 
b=("Nokia","Vivo","Samsung","Motorola","Realme","Redmi","Poco")
print(b[1::])
print(b[::-1])
print(b[1::2])
print(b[-5:-2:2])

#using for loop
for i in b:
    print(i)
print("*"*40)
    
#also
for i in range(len(b)):
    print(b[i])
print("~"*40)

#using while loop
i=0
while i<len(b):
    print(b[i])
    i+=1