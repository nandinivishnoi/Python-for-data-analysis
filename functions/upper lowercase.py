def count_uppercase_lowercase(sentence : str)-> dict:
    count={"No. of upper elements" : 0,
           "No. of lower elements" : 0}
    for s in sentence:
        if s.isupper():
            count["No. of upper elements"]+=1
        elif s.islower():
            count["No. of lower elements"]+=1
    return count
print(count_uppercase_lowercase("She was studying IN Her ROOM" ))
    