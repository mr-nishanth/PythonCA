print("Enter Your Guess's format is [ dd-mm-yyyy ]")
print("Note:'Single digit means prefix 0 not necessary [eg: 1-1-1111]'")
MyDOB = "9-7-2000"
Count = 1
Total_Life = 10
Mark = 100
extraMark = 0
while Count<=10:
    INPUT = input("Enter your Guess : ")
    if MyDOB != INPUT:
        Total_Life -= 1
        Mark -= 10
        print(" Oopp's Incorrect , Try Again ")
        print(f"{Total_Life} is Remaining...")
    else:
        print(" WOW! Well done Dear ....")
        print(f"Congrate you have won in {Count} Life")
        break
    Count += 1
if Total_Life <= 0:
    print(" ---X---X---X--->Game Over <---X---X---X---")
elif Total_Life <= 5:
    print(f"Your Total Score {Mark}")
elif Total_Life > 5 and Total_Life <= 8:
    extraMark+=25
    print(f"Hurry!.. Your Total Score is {Mark} + Extra Score {extraMark} = {Mark+extraMark} ")
elif Total_Life > 8 and Total_Life <= 9:
    extraMark+=75
    print(f"Hurry!.. Your Total Score is {Mark} + Extra Score {extraMark} = {Mark+extraMark} ")
else:
    extraMark+=100
    print(f"Hurry!.. Your Total Score is {Mark} + Extra Score {extraMark} = {Mark+extraMark} ")