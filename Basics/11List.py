# Mutable           ---> Can Change
# Immutable         ---> Cannot Change

# Grocery = ["Harpic","Soap","Dabba","Deodarant","Potato","Lollipop"]
# print(Grocery)
# for i in Grocery:
#     print(i)

# num = [21,45,3,6,2,7,4,8,3,9,4]
# print(num)
# print(num.sort())
# num.sort()
# print(num)
# print(num.reverse())
# num.reverse()
# print(num)

# print(num[::-1])
# print(num[1:5:2])

# num1 =list()
# num1.append(666)
# num1.append(777)
# num1.append(888)
# print(num1)

# #Object_name.insert(Index,Value)
# num1.insert(3,999)
# print(num1)
# #Object_name.remove(Value)
# num1.remove(888)
# print(num1)

# #Object_name.pop(Index)
# num1.pop(1)
# print(num1)

# num1[0]=333
# print(num1)

# Tuples

TP = tuple()
TP=(1,2,3,4,5)
print(TP, " ", type(TP))

TO = (7)
print(TO, " ", type(TO))
TO = (7,)
print(TO, " ", type(TO))

# Swap two Number
a = 1
b = 2
a, b = b, a
print(a)
print(b)