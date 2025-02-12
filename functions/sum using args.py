def sum_ls(*args ):
    sum=0
    for number in args:
        sum=sum+number
    return sum 
print(sum_ls(10,20,10,5))