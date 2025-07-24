price = 0
BASIC = 5
STANDARD = 10
DELUXE = 15
WAX = 4


TYPE = input("Welcome to our car wash. How can we be of assistance today?\nPlease enter B for a basic wash, S for a standard wash and D for our deluxe offering. ")

if TYPE.upper() == "B":
    price = BASIC
    print(f"That will be ${price} for our basic wash option.")
elif TYPE.upper() == "S":
    price = STANDARD
    print(f"That will be ${price} for our standard wash option.")
elif TYPE.upper() == "D":
    price = DELUXE
    print(f"That will be ${price} for our deluxe option.")

extra = input("Would like a wax and polish with that? Please enter Y or N: ")
if extra.upper() == "Y":
    price = price + WAX
    print(f"That will be an additional ${WAX}.  Your final price will be ${price}")
else:
    print(f"Thank you for your patronage. Your final price will be ${price}")
