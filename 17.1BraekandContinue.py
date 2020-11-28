i = 1
while True:
    if i%10==0:
        print(i)
        break
    i+=1

for i in range(1,21):
    if i==10:
        continue
    print(i)


while True:
    Input = int(input("Enter your age : "))
    if Input < 18 or Input >70 :
        print("Sorry for that .. ")
        continue
    else:
        print(" Say wow! ")
        break