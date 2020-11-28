Product = "Realme Narzo 21 pro , Rs.17K , 65W-Fast Charge"
Moblie_Name = Product[: Product.index(',')]
print(Moblie_Name)

Moblie_Price = Product[Product.index(',') +1 :]
print(Moblie_Price)

# Index     --> Search First Index  Like Forward Checking
# R-Index   --> Search Last Index   Like Backward Checking
Moblie_Price = Product[Product.index(',') +1 :Product.rindex(',')]
print(Moblie_Price)
Moblie_Battery = Product[Product.rindex(',')+1:]
print(Moblie_Battery)