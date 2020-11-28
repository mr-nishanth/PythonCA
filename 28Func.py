# 4. Variable Length
# *Variable_name --> It's is Variable Length Arguments
# Store in Tuples
print("Learn Variable Length Arguments")
def add(a, *b):  # *b is tuples
    """ It's is Variable Length Arguments """
    for i in b:
        a=a + i
    print(a)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(sum((1,2,3,4,5,6,7,8,9,10)))  # In Sum function we will pass tuple-type Values only Like (10,20,30)
print("======================================================")