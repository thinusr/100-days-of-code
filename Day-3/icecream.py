price = 0

print("Welcome to my ice cream stand!")

icecream = input("Please enter what size ice cream you would like to buy? S, M or L\n")

if icecream.upper() == "S":
    price += 3
    print(f"That will be ${price} for a small ice cream.")
elif icecream.upper() == "M":
    price += 5
    print(f"That will be ${price} for a medium ice cream.")
elif icecream.upper() == "L":
    price += 7
    print(f"That will be ${price} for a large ice cream.")

toppings = input("Would you like some chocolate sprinkles on that? Enter Y or N\n")
if toppings.upper() == "Y":
    price += 1
    print (f"Thank you for your patronage. The total price for your ice cream will be ${price}")

if icecream.upper() =="L" and toppings.upper() =="Y":
    print("Go big or go home!  Enjoy your deluxe treat!")
else:
    print("Enjoy your ice cream!")
