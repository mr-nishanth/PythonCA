Var = "I am a Good Boy"
print(Var)
print(Var.index("G"))
#print(Var.index("g")) # Avoid Error throung using find
# Object.Replace(old,new)
print(Var.replace("Good", "Bad"))
print(Var.find("B"))
print(Var.find("b"))

product = "Asus Rob, Rs 100k, new"

# [Start-to:when you see comma symbol Stop that place]
name = product[: product.index(",")]
print(name)
