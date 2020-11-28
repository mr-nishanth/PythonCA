class Father:
    soccer=1

class Son(Father):
    dance = 1
    def dancer(self):
        dance_name=input("What type of dance you like : ")
        return f"I Like {dance_name} dance"

class GrandSon(Son):
    dance=6

dad = Father()
son = Son()
kaka = GrandSon()
print(kaka.soccer)
print(kaka.dancer())
