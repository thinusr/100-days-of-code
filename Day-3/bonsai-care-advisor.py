print("Welcome to our Bonsai Care Advisor!")
species = input("Which of your trees do you need help with today?\nPlease enter Spekboom, Acacia or Boxwood: ").lower()

if species == "spekboom":
    dry = input("Is the soil completely dry? (Y/N): ").lower()
    if dry == "y":
        print("Water it thoroughly.")
    elif dry == "n":
        print("Wait another day or two before watering.")
elif species == "acacia":
    leaves = input("Is it dropping leaves? (Y/N): ").lower()
    if leaves =="y":
        print("It might need more sunlight, or it could be getting too much water.")
    elif leaves == "n":
        print ("Continue normal care.")
elif species == "boxwood":
    leaves = input("Are the leaves turning yellow? (Y/N): ").lower()
    if leaves == "y":
        print("Check for root rot or poor drainage.")
    elif leaves == "n":
        print("All good!")


else:
    print("I'm sorry, but I can not help you with that species at the moment.  Please check again later.")
