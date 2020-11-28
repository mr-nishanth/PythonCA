# read ; readline print line by line ; readlines  --> Convert to List

File = open("FirstFile.txt", mode="rt")
print(File.readline())
print(File.readline())
print(File.readline())
print(File.readlines())

# File_Pointer.read(take_Args)  ==> take_Args -->How many Char you need to read
# content = File.read(10)
# print(content)
# content = File.read(20)
# print(content)
for line in File:
    print(line, end="")
#VideoFile = open("Azhage.mp4", mode="rb")
#Text = VideoFile.read()
#print(Text)  # Waring Alert