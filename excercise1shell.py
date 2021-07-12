name = input("what is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword =['passwordSeyi','passwordMike','passwordLove']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)       

    if(password == allowedPassword[userId]):
        print("Welcome %s" % name)
    else:
        print("Password incorrect, please try again")

else:
    print("Name not found, please try again")        




        # pseudocode here
