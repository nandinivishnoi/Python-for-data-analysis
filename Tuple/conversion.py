#as tuple is immutable we need to convert it into a list first to make any changes in it

b=("Nokia","Vivo","Samsung","Motorola","Realme","Redmi","Poco")
print(b,type(b))

b=list(b)
print(b,type(b))

#now we can make changes in the converted tuple for example
b.append("Google pixie")
print(b)

b.insert(3,"One plus")
print(b)

b.remove("Vivo")
print(b)

b.pop(4)
print(b)

b.sort()
print(b)
#and many more!