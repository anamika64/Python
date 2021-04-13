import function1 as o
while True:
    print("********************calculator**************************")
    print("+ for addition")
    print("- for substraction")
    print("* for mul")
    print("/ for div")
    print("//for fdiv")
    print("% for mod")
    print("** for power")
    ch=input("Enter your choice=> ")
    if ch=='+':
        o.add()
    elif ch=='-':
        o.sub()
    elif ch=='*':
        o.mul()
    elif ch=='/':
        o.div()
    elif ch=='//':
        o.fdiv()
    elif ch=='%':
        o.mod()
    elif ch=='**':
        o.exp()
    elif ch=='q' or ch=='Q':
        break
    else:
        print(" no such choice")
        
