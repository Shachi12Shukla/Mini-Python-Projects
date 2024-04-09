# Snake Water Gun Game !
import random
import time
print("Ready to play?")
time.sleep(1)
print("SNAKE\n")
time.sleep(1)
print("WATER\n")
time.sleep(1)
print("GUN!!!?\n")
time.sleep(2)
no_of_chances = int(input("Enter the number of rounds you want to play the game\n "))
lst = ["snake", "water", "gun"]
computer_choice = random.choice(lst)
i=0
count1 = 0
count2 = 0
while(i <= no_of_chances):
    var1 = "snake"
    var2 = "water"
    var3 = "gun"
    
    user_response = input(f"Enter {var1}, {var2}, or {var3}\n")
    if user_response == var1 and computer_choice == var2:
        print("You won a point!")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count1 += 1
        
    elif user_response == var2 and computer_choice == var1:
        print("Oops! computer won a point")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count2 += 1
        
    elif user_response == var1 and computer_choice == var3:
        print("Oops! the computer won")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count2 += 1
       
    elif user_response == var3 and computer_choice == var1:
        print("Yay! you won a point!")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count1 +=1
        
    elif user_response == var2 and computer_choice == var3:
        print("Yay! you won a point!")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count1 += 1
        
    elif user_response == var3 and computer_choice ==var2:
        print("Oops! the computer won a point!")
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")
        count2 += 1

    elif user_response == computer_choice:
        print("A tie! so both won 0 points ") 
        print(f"Your guess is {user_response} and computer guess is {computer_choice}")   

    else:
        print("Try again!\n")
        
    i = i+1  
    print(f"your point(s) is {count1} and computer point is {count2}\n")
    print("Do you want to exit from the game? \n")
    ans1 = 'yes' 
    ans2 = 'no'
    ans = input(f"Enter {ans1} or {ans2} ")
    if ans==ans1:
        print("You have exited from the game")
        break
    elif ans==ans2:
        print("The game continues...")
    else:
        print("Enter a valid response!")
    
if count1==count2:
    print("A tie! ")
elif count1>count2:
    print("You won the game !")
elif count2>count1:
    print("The computer won \nBetter luck next time!")
print(f"Your total score is {count1} and computer score is {count2}")
print("Thank you for playing :) ")
