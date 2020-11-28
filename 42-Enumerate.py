# Enumerate function ==> Index start from zero(0)
# ( is not ) == ( != )  Both are same

# List = ["Potato", "Tomato", "Biscuit", "Kurkure", "Pizza"]
# S = 1
# for i in List:
#     if S % 2 != 0:
#         print(i)
#     S+=1
# print("===============================")
# s = 1
# for Items in List:
#     if S % 2 == 0:
#         print(Items)
#     s+=1

List = ["Potato", "Tomato", "Biscuit", "Kurkure", "Pizza"]

for index, items in enumerate(List):
    if index%2 is 0:
        print(items)
    # elif index % 2 is not 0:
    #     print(items)
    else:
        pass
