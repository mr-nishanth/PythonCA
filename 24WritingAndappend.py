# File_Pointer = open()

# W mode is to create a new file
File = open("second.txt", mode="wt")
File.write("India is A developed Country")
File.write("\nWe can Change this world..")
File.close()

print("Write-Mode")
newFile = open("WriteMode.txt", mode="wt")
newFile.write("Hurry\n")
newFile.write("WOW\n")
newFile.write("Oop's\n")

print("Append-Mode")
newFile = open("WriteMode.txt", mode="at")
newFile.write("I love Football \n")

