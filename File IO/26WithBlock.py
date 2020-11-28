# With main Usage close() is not needed
# Here f is a File-Pointer
with open("FirstFile.txt") as f:
    print(f.readline())
File = open("FirstFile.txt", mode="rt")
print(File.readline())
File.close()
