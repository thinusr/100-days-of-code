ticket = 0

print("Welcome to the cinema. ")

age = int(input("Please enter you age: "))

if age < 13:
    ticket += 5
    print(f"Your ticket will cost ${ticket}")
elif age <= 17:
    ticket += 7
    print(f"Your ticket will cost ${ticket}")
elif age <= 64:
    ticket += 12
    print (f"Your ticket will cost ${ticket}")
else: 
    ticket += 6
    print("You qualify for senior's discount.")
    print(f"Your ticket will cost only ${ticket}")

D3 = input("Would you like to watch this movie in 3D? Please answer Y or N: ")

if D3.upper() == "Y":
    ticket += 3
    print(f"That will be an extra $3.  Your total is now: ${ticket}")
else: 
    print("No extra charge for 2D")

print("Enjoy your movie!")


