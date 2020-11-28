# String Slicing--> Using Index

String = "Welcome to Learn String Slicing"
print(String)
print(String[-1])
# [Start(n) : Stop (n-1)]
print(String[11:])
print(String[:9])

# Default Starting (0) : Stop (full)
print(String[:])

print("------------------(Jumping)-----------------")
# [Start(n) : Stop (n-1) : Jump(n-1)]
print(String[::1])
print(String[::2])
print(String[::3])
print(String[::4])

print("--> String Revearse for <--")
print(String[::-1])