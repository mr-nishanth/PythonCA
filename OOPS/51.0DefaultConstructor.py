class Fun():
    def __init__(self):
        print("Default constructor")
    def add(self):
        print("Adding")
c = Fun()
print(c.__dict__)
c.add()