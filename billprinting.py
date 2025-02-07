#write a program to print customers bill

while True:
    name=input("Enter customers name: ")
    total=0
    while True:
        print("Enter amount and quantity")
        quantity=float(input("number of iteam: "))
        amount=float(input("amount: "))
        total+=quantity*amount
        repeat=input("do you want to add more items (yes/no): ")
        if(repeat=="no" or repeat=="NO"):
            break
    print("-" * 40)
    print("Customer name: ",name)
    print("Total bill to be paid: ",total)
    print("-" *40)
    print("HAPPY SHOPPING")
    print("*" *30)
    repeat=input("Do you want to bill another customer (yes/no): ")
    if(repeat=="no" or repeat=="NO"):
        break