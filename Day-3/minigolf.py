print("Welcome to our mini golf course!")
price = int(0)
clubs = int(3)
age = int(input("Please enter your age. "))
if age < 4:
    price += 0
    print(f"A round of golf will cost you ${price}")
elif age <= 12:
    price += 5
    print(f"A round of golf will cost you ${price}")
elif age <= 17:
    price += 7 
    print(f"A round of golf will cost you ${price}")
elif age <= 64:
    price += 10
    print(f"A round of golf will cost you ${price}")
else:
    price += 6
    print(f"You qualify for our senior's discount.  A round of golf will only cost you ${price}")

rental = input(f"Would you like to rent some clubs at an additional ${clubs}? Please enter Y or No: ")

if rental.upper() == "Y":
    price += 3
    print(f"Your total price is ${price}")
else:
    print(f"Your total price remains ${price}")

print("Enjoy your round of mini golf!")
