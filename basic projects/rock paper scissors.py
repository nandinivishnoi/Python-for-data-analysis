import random
print("""Enter what to choose
      1. Rock
      2. paper
      3. scissors""")
a={1: "Rock",
   2: "Paper",
   3: "Scissors"}
actions=["Rock","Paper","Scissors"]

com_input=random.choice(actions)
user_input=int(input("Enter your choice: "))
map_input=a[user_input]
print("computer Response was: ", com_input)

if map_input==com_input:
    print("Its a tie")
elif map_input=="Rock":
    print("Yaayyyyyyy!! you have won")
elif map_input=="Scissors":
    if com_input=="Rock":
        print("You lost")
    elif com_input=="Paper":
        print("Yaaay: you won!!11")
        print("*"*20, "Congratulations","*"*20)
elif map_input=="Paper":
    print("You loose")