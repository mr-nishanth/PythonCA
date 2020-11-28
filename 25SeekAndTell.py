# Tell () --> Tell the where is  my file_ponter
File_Pointer = open("FirstFile.txt")
print("Starting File-Pointer",File_Pointer.tell())
print(File_Pointer.readline())
print(File_Pointer.tell())
print(File_Pointer.readline())
print(File_Pointer.tell())
File_Pointer.close()  # File Closing is Important

# Seek()  --> used for control the file_pointer
file_Pointer = open("WriteMode.txt", mode="rt")
print(file_Pointer.readline())
file_Pointer.seek(4)
print(file_Pointer.readline())
file_Pointer.close()