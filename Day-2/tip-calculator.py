print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
multiplier = 1 + (tip / 100)
total_bill = bill * multiplier
split = input("How many people to split the bill? ")
per_person = round(total_bill / int(split), 2)
print(f"Each person should pay: ${per_person}")
