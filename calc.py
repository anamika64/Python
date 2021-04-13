print("**************calculator****************")
print("1 + for addition")
print("2 - for substraction") 
print("3 * for multiplication")
print("4 / for division")
print("5 // for floor division")
print("6 ** for exponential")
print("7 % for modulo")
ch=input("Enter your opration =")
if ch =="1":
       x=int(input("Enter value for x="))
       y=int(input("Enter value for y="))
       s=x+y
       print("addirion of {} + {} = {}".format(x,y,s))
elif ch=="2":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x-y
    print("addirion of {} - {} = {}".format(x,y,s))
elif ch=="*":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x*y
    print("addirion of {} * {} = {}".format(x,y,s))
elif ch=="/":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x/y
    print("addirion of {} / {} = {}".format(x,y,s))
elif ch=="//":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x//y
    print("addirion of {} // {} = {}".format(x,y,s))
elif ch=="**":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x**y
    print("addirion of {} ** {} = {}".format(x,y,s))
elif ch=="%":
    x=int(input("Enter value for x="))
    y=int(input("Enter value for y="))
    s=x%y
    print("addirion of {} % {} = {}".format(x,y,s))
else:
    print("invalid ...")
