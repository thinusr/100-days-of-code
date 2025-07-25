small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_medium_large = 3
cheese = 1
price = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size.upper() == "S":
    price += small
elif size.upper() == "M":
    price += medium
elif size.upper() == "L":
    price += large

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.upper() == "Y" and size.upper() == "S":
    price += pepperoni_small
elif pepperoni.upper() == "Y" and size.upper() == "M":
    price += pepperoni_medium_large
elif pepperoni.upper() == "Y" and size.upper() == "L":
    price += pepperoni_medium_large

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese.upper() == "Y":
    price += cheese

print(f"Thank you for shopping with Python Pizza.  Your final bill will be ${price}")
