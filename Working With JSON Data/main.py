import json


def createAccount():
    newUser = {}
    newUser["name"] = input("\nEnter Your Name : ")
    newUser["age"] = int(input("\nEnter Your Age : "))
    newUser["email"] = input("\nEnter Your Email : ")

    for dic in fileData["users"]:
        if newUser["email"] == dic["email"]:
            print("Email Already Exists")
            return
    else:
        newUser["password"] = input("\nEnter Your Password : ")
        conPassword = input("\nConfirm Your Password : ")

        if newUser["password"] != conPassword:
            print("Password and Confirm Password should be same")
            return
        fileData["users"].append(newUser)

        # Writing Data To JSON File
        with open("data.json", "w+") as f:
            data = json.dump(fileData, f)
        print("User Created Successfully")


def signIn():
    email = input("\nEnter Your Email : ")
    password = input("\nEnter Your Password : ")

    for dic in fileData["users"]:
        if email == dic["email"]:
            if password == dic["password"]:
                print("Signed in Successfully")
                return

    print("Invalid Credentials")
    return


choice = int(input(
    "Welcome To PyUser Management System\nChoose 0 For Sign in\nChoose 1 For Creating New Account : "))


# For Reading Data From JSON File
with open("data.json", "r") as f:
    fileData = json.load(f)


if choice == 1:
    createAccount()
elif choice == 0:
    signIn()
else:
    print("Invalid Choice")
