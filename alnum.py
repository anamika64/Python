while(True):
    password=input("Enter password:")
    if(password.isalnum()):
        print("valid")
        break
    else:
        print("not a valid,please renter the pssword ")
