print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in meters: "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter you age: "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")