def unique_number(num):
    ls=set()
    for n in num:
        ls.add(n)
    return list(ls)

print(unique_number([1,2,3,4,4,3,3,3,3,6,4,]))