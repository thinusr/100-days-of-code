price = 0
BASIC = 10
STANDARD = 15
PREMIUM = 25
SLEEPING_BAG = 5

rental = input("Welcome to Campfire Gear Rental. You can choose from our range of gear packages.\nPlease enter B for our BASIC package, S for our STANDARD package or P for the PREMIUM package. ")

if rental.upper() == "B":
    price = BASIC
    print(f"Thank you for choosing our basic package. The price for this package is ${price}")
elif rental.upper() == "S":
    price = STANDARD
    print(f"Thank you for choosing our standard package.  The price for this package is ${price}")
elif rental.upper() == "P":
    price = PREMIUM
    print(f"Thank you for choosing our premium package.  The price for this package is ${price}")
else:
    print("Sorry that is not a valid package option.")
    exit()

bag = input("Would you like to add a sleeping bag to your package? Enter Y or N: ")

if bag.upper() == "Y":
    price = price + SLEEPING_BAG
    print(f"Thank you for choosing this option.  Your final bill is ${price}")
else:
    print(f"Thank you for choosing Campfire Gear Rental! Your final bill is ${price}")
