def login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        print("Username or Password cannot be blank")
    else:
        if user == "admin":
            if pwd == "pass123":
                print("Login Successful")
            else:
                print("Invalid Password")
        else:
            print("Invalid Username")

user = input("Enter username: ")
pwd = input("Enter password: ")
login(user, pwd)