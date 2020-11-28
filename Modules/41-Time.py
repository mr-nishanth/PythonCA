import time
Initial = time.time() # Returns Sec
print(Initial)  # Like before Start writing time
k = 0
while k < 50:
    print("I'm a Bad Boy",end=" ")
    k += 1
    time.sleep(2)
print(f"Time for execution of while loop => {time.time()-Initial}") # Current_time - before Start writing time
initial = time.time()
print(initial)
for i in range(50):
    print("I am Bad Boy", end=" ")
    time.sleep(2)
print(f"Time for execution of for loop => {time.time()-initial}")

"""
time.asctime --> Convert to Sun Nov 22 15:31:24 2020 this format
time.localtime --> Return Current time in Tuple format
time.time()  --> Convert to Railway Time
"""
LocalTime = time.localtime(time.time())
print(LocalTime)
LocalTime = time.asctime(time.localtime(time.time()))
print(LocalTime)
