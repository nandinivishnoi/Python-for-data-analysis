def multiply(*args):
    mul=1
    for number in args:
        mul=mul*number
    
    return mul
print(multiply(2,3,5,7))