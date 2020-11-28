def printEvenAndOddNum(List):
    """ Find the number if number's is even or odd, then append separate list and find the number of  even and odd numbers """
    even, evenCount = 0, 0
    odd, oddCount = 0, 0
    evenList = list()
    oddList=list()
    for i in List:
        if i % 2 == 0:
            evenCount += 1
            evenList.append(i)
        else:
            oddCount += 1
            oddList.append(i)
    return f"Even Numbers are : {evenList} and Total Number of even no are : { evenCount}\nOdd Numbers are : { oddList} and Total Number of odd no are : {oddCount}"
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(printEvenAndOddNum(List))
print(printEvenAndOddNum.__doc__)