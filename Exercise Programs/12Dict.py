# Real-Life Example ==> Saving Phone Numbers

PhoneBook = {"Police": 100, "Fire": 102, "Nisha" : 161}
Key = input("Enter the name of the person whose number you want ? : ").title()
print(f"The number of {Key} is {PhoneBook.get(Key)}")