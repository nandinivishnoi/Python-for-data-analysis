def factorial(number):
    if number<=1:
        print(number)
    else:
        fact=1
        while number>=1:
            fact=fact*number
            number-=1
    return fact
print(factorial(5))