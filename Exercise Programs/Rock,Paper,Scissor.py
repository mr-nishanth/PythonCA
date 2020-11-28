#List = ['Rock', 'Paper', 'Scissor']

import random
List = ['W', 'G', 'S']
chance=10
no_of_chance = 0
computer_point=0
human_point = 0
H = "Human"
C = "Computer"
print("""
            'Snake' as S
            'Water' as W
            'Gun' as G
    """)
while no_of_chance < chance:
    _random = random.choice(List)
    userInput = input("Enter your guess : ").upper()
    if userInput == _random:
        print(f"Your Guess {userInput} and  computer guess {_random} \n")
        print(" Tie Both 0 points to each \n")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
# if User Enter S
    elif userInput == "S" and _random == "G":
        computer_point += 1
        print(f"Your Guess {userInput} and  computer guess {_random}\n ")
        print(f"{C} win Total {computer_point} points\n ")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
    elif userInput == "S" and _random == "W":
        human_point+=1
        print(f"Your Guess {userInput} and  computer guess {_random}\n ")
        print(f"{H} win Total {human_point} points \n")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
# if User Enter W
    elif userInput == "W" and _random == "S":
        computer_point += 1
        print(f"Your Guess {userInput} and  computer guess {_random} \n")
        print(f"{C} win Total {computer_point} points \n")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")

    elif userInput == "W" and _random == "G":
        human_point += 1
        print(f"Your Guess {userInput} and  computer guess {_random}\n ")
        print(f"{H} win Total {human_point} points\n ")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
# if User Enter G
    elif userInput == "G" and _random == "S":
        human_point += 1
        print(f"Your Guess {userInput} and  computer guess {_random} \n")
        print(f"{H} win Total {human_point} points \n")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
    elif userInput == "G" and _random == "W":
        computer_point += 1
        print(f"Your Guess {userInput} and  computer guess {_random} \n")
        print(f"{C} win Total {computer_point} points \n")
        print(f"{C} point is {computer_point} and {H} point is {human_point}\n")
    else:
        print("You have input wrong \n")
    no_of_chance += 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
    print(f"========> Round NO : {no_of_chance +1} <=======")
if computer_point == human_point:
    print("Tie")
elif computer_point > human_point:
    print(F" Opps!.. {C} Won the Match\n ")
else:
    print(F" Hurry!.. {H} Won the Match\n")

print(f" {H} point is {human_point} and {C} point is {computer_point}\n")
