print("*********************Welcome to Dominoz**************************")
list1=[]
while True:
    
    print(" 1 Your order is for Veg")
    print(" 2 Your order is for Non-Vage")
    print(" 3 for no")

    ch=int(input("Enter your choice=> "))
    a = 'cheesse pizza'
    b = 'paneer pizza'
    c = 'barbque pizza'
    d = 'chicken pizza'
    if ch==1:
        while True:
            print("a.",a)
            print("b.",b)
            print("n. for no")
            ch=input("Enter your choice=> ")
            if ch=='a':
                print(a)
                print('order placed')
                list1.append(a)
            elif ch=='b':
                print(b)
                print('order placed')
                list1.append(b)
            elif ch=='n':
                print("nothing order")
                break
            else:
                print("no operation found")




    elif ch==2:
        while True:
            print("a.",c)
            print("b.",d)
            print("n. for no")
            ch=input("Enter your choice=> ")
            if ch=='a':
                print(c)
                print('order placed')
                list1.append(c)
            elif ch=='b':
                print(d)
                print('order placed')
                list1.append(b)
            elif ch=='n':
                print("nothing order")
                break
            else:
                print("no operation found")



    elif ch == 3:
        break

    else:
        print("invalid input")


        
print(list1)




    
