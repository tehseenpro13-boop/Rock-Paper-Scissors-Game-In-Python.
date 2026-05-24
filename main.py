'''
1 is for rock
2 is for paper
3 is for scissors

'''

import random

score = 0
count = 0
c_score = 0
c_count = 0
d_count = 0
for i in range(1,11):
 computer = random.choice([1,2,3])
 num = {1,2,3}
 youstr = input("Enter your Choice :")
 youdict = {"r":1,"p":2,"s":3}
 reversedict = {1:"rock",2:"paper",3:"scissors"}
 you = youdict[youstr]
 print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")
 if(computer==you):
    d_count = d_count + 1
    with open("Project_1/Draws.txt", "w") as f:
        f.write(str(d_count))
    print("Draw!")
 else:
    if(computer==1 and you==2):
        count = count + 1
        with open("Project_1/wins.txt", "w") as f:
            f.write(str(count))
        score = score + 10
        print("You Win!")
        with open("Project_1/Score.txt", "w") as f:
            f.write(str(score))

    elif(computer==3 and you==1):
        count = count + 1
        with open("Project_1/wins.txt", "w") as f:
            f.write(str(count))
        score = score + 10
        print("You Win!")
        with open("Project_1/Score.txt", "w") as f:
            f.write(str(score))
    elif(computer==2 and you==3):
        count = count + 1
        with open("Project_1/wins.txt", "w") as f:
            f.write(str(count))
        score = score + 10
        print("You Win!")
        with open("Project_1/Score.txt", "w") as f:
            f.write(str(score))
    elif(computer==1 and you==3):
        c_score = c_score + 10
        with open("Project_1/c-score", "w") as f:
            f.write(str(c_score))
        c_count = c_count + 1
        with open("Project_1/c-wins", "w") as f:
            f.write(str(c_count))
        print("You Loose!")
    elif(computer==2 and you==1):
         c_score = c_score + 10
         with open("Project_1/c-score", "w") as f:
            f.write(str(c_score))
         c_count = c_count + 1
         with open("Project_1/c-wins", "w") as f:
            f.write(str(c_count))
         print("You Loose!")
    elif(computer==3 and you==2):
         c_score = c_score + 10
         with open("Project_1/c-score", "w") as f:
            f.write(str(c_score))
         c_count = c_count + 1
         with open("Project_1/c-wins", "w") as f:
            f.write(str(c_count))
         print("You Loose!")

    else:
        print("Somethig Went Wrong")  

print("\nROUND OVER\n") 
print(f"Your Final Score is {score}!")
print(f"You won {count} games!")
print()
print(f"Computer Final Score is {c_score}!")
print(f"Computer Won {c_count} games!")
print()
print(f"{d_count} Games were a Draw!")
print()