year=int(input("Enter year ="))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("year {} is leap year".format(year))
        else:
            print("year {} is not leap year". format(year))
    else:
        print("year {} is leap year".format(year))
else:
    print("year {} is not leap year".format(year))
