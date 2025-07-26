# Use this script as an example of structure.

main_choice = input("Choose something: option1 / option2 / option3\n").lower()

if main_choice == "option1":
    sub_choice = input("More detail about option1? Y/N: ").lower()
    if sub_choice == "y":
        print("Do this...")
    elif sub_choice == "n":
        print("Do that...")
    else:
        print("Invalid input.")
        
elif main_choice == "option2":
    print("Do something else.")

elif main_choice == "option3":
    print("Handle a third case.")

else:
    print("Invalid selection.")

