def Sub(A=0,B=0):  # Called Func
    print(A-B)
    return A-B
Sub(100,55)  # Calling Func
C = Sub(55,35)
print(C)

'''
  Actual Arguments
1. Position
2. Keyword
3. Default
4. Variable Length

'''

# 1. Position
print("Learn position Arguments")
def bio_Data(name, age):
    """ Position Arguments """
    print(f"Your name is {name} and {age} year's old... ")

bio_Data("Nisha",20)
print("======================================================")

# 2. Keyword
print("Learn Keyword Arguments")
def bio_Data(name, age):
    """ Keyword Argument """
    print(f"Your name is {name} and {age - 1} year's old... ")

bio_Data(age=19, name="Nishanth")
print("======================================================")

# 3. Default
print("Learn Default Arguments")
""" Default Arguments """
def bio_Data(name="Please type your name ", age=18):
    print(f"Your name is {name} and {age - 1} year's old... ")

bio_Data(name="Cyber-Nishanth",age=25)
print("======================================================")

