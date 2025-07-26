# Just me playing around with some ideas.
# This is not a working script.

issue = input("Good day!\nWhat issues are you having with your Linux system today?\nwifi / audio / display\nPlease enter you selection now.\n")
if issue == "wifi":
    wifi_follow_up = input("Is your wifi adapter visible? Enter yes or no. ")
    if wifi_follow_up == "yes":
        print("Enter your wifi SSID and password.")
    elif wifi_follow_up == "no":
        print("Try running: 'sudo lshw -C network'")
elif issue == "display":
    display_follow_up = input("Is your monitor connected? Enter yes or no. ")
    if display_follow_up == "yes":
        display_server = input("Which display server are you using? Enter X11 or wayland. ")
        if display_server == "X11":
            print("run 'xprop' in your terminal to see which monitors are connected.")
        elif display_server == "wayland":
            print("Sorry.  I know nothing about wayland.")
    elif display_follow_up == "no":
        print("Try connecting your monitor.")
