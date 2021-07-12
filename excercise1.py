name = input("what is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = "Password"


if(name in allowedUsers):
    password = input("Your password? \n")

    if(password == allowedPassword):
        print("Welcome %s" % name)
    else:
        print("Password incorrect, please try again")

else:
    print("Name not found, please try again")        




        # pseudocode here
        # you can manually run your code by typing python text.py inside terminal
