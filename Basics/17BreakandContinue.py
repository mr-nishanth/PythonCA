i = 1
while True:
    print(i)
    i += 1
    if i > 100:
        print("Battery Over-Charging",end=" , ")
        print("Waring Alert !........ ")
        break
j=1
while True:
    if j > 25 and j < 27:
        print(f"{j}  Precentage Completed ")
    elif j > 50 and j < 52:
        print(f"{j}  Precentage Completed ")
    elif j > 75 and j <77:
        print(f"{j} Precentage Completed ")
    elif j == 100:
        print(f" {j} Precentage Completed Full Charged ..")
    else:
        print("Battery Over-Charging", end=" , ")
        print(j)
        print("Waring Alert !........ ")
        break
    j = j + 1

Count = 1
while True:
    k = int(input("Enter the  numbers : "))
    if k > 100:
        print(f"Congratulations you Reached {k} Subscribe's...")
        break
    else:
        print("All the Best , You will Need More Subs")
        continue