import random
chances=5

print (''' Choose the level of the game
1. Easy
2. Hard
3. Extreme''')

level=int(input())

if level==1:
    ran=random.randint(0,50)
elif level==2:
    ran=random.randint(0,100)
elif level==3:
    ran=random.randint(0,200)   
    
print("you selected game level",level)   
    
while(chances):
    chances-=1
    user_inp=int(input("What do you think the number is?: "))
    if(user_inp<ran):
        print("the number you have entered is less", "chances left = ", chances) 
    elif(user_inp>ran):
        print("The number you have entered is greater", "chances left = ", chances)
    elif(user_inp==ran):
        print("Yaaaaaaaaaaaaaayyyyy!,You got it correct")
        print("*"*10 ,"CONGRATULATIONS" ,"*"*10)
        break
        
print("The number was",ran)