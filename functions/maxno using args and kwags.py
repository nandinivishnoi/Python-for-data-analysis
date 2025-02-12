def max_number(*args, **kwags):
    max_num=-1
    for number in args:
        if number > max_num:
            max_num=number
            
    return max_num
print(max_number(23,54,12,34,89,67,90,45,36))