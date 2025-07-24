quick_wash = 5
regular_wash = 8
heavy_wash = 12
dry = 3

wash = input("Thank you for trying Lyttelton Laundromat.\nPlease choose one of the following options.\nQ for a quick wash, R for a regular wash or H for a heavy duty wash: ")

if wash.upper() == "Q":
    price = quick_wash
    print(f"Thank you for choosing our quick wash option.  The price for this service is ${price}")
elif wash.upper() == "R":
    price = regular_wash
    print(f"Thank you for choosing our regular wash option.  The price for this service is ${price}")
elif wash.upper() == "H":
    price = heavy_wash
    print(f"Thank you for choosing our heavy duty wash option.  The price for this service is ${price}")
else:
    print("Sorry, this is not a valid option.  Please try again.")
    exit()

extra = input(f"Would you like to use our drying service at an additional ${dry}?  Please enter Y for YES or N for NO: ")
if extra.upper() == "Y":
    price += dry
    print(f"Thank you for choosing this option.  Your total bill is ${price}")
else:
    print(f"Thank you for your patronage.  Your total bill is ${price}")
