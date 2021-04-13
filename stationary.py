print("1 for Pen Rs. 20/-")
print("2 for Book Rs. 45/-") 
print("3 for Colors Rs. 90/-")
x=int(input("Enter the item you want to purchase="))
if x==1:
    qty=int(input("Enter number of quantity of Pen:"))
    bill_amt=20*qty
    print("***********Stationary Bill****************")

    print("bill_no=",1234)
    print("Item    qty   Price\t"    "Total")
    print("Pen      {}    20          {}".format(qty,bill_amt))
elif x==2:
    qty=int(input("Enter number of quantity of Books:"))
    bill_amt=45*qty
    print("***********Stationary Bill****************")

    print("bill_no=",1234)
    print("Item    qty   Price\t"    "Total")
    print("Book      {}    20          {}".format(qty,bill_amt))
elif x==3:
    qty=int(input("Enter number of quantity of Color:"))
    bill_amt=90*qty
    print("***********Stationary Bill****************")

    print("bill_no=",1234)
    print("Item    qty   Price\t"    "Total")
    print("Color      {}    45          {}".format(qty,bill_amt))
else:
    print("Item does not available")




    
