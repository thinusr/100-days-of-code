child_ticket = 5 # under 12
youth_ticket = 7 # 12-18
adult_ticket = 12 # 18 and over
price = 0
photo = 3

print("Welcome to the rollercoaster ride!")
height = int(input("Please enter your height in cm. "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age: "))
    if age < 12:
        price = child_ticket
        print(f"Your ticket price will be ${price}")
    elif age < 18:
        price = youth_ticket
        print(f"Your ticket price will be ${price}")
    else:
        price = adult_ticket
        print (f"Your ticket price will be ${price}")

    wants_photo = input(f"Would you like your photo taken at an additional ${photo}? Enter Y for Yes and N for No. ")
    if wants_photo.upper() == "Y":
        print(f"Thank you for choosing this option.  Your final bill will be ${price + photo}")
    else:
        print(f"Thank you for your patronage.  Your final bill will be ${price}")

else:
    print("Sorry, you are too short for this ride and need to grow taller.")
