def display(Num):



   



   if Num % 3 == 0 and Num % 5 == 0 :



       print("Zoom")



       



   elif Num % 3 == 0 :



       print("Zip")



   



   elif Num % 5 == 0 :



       print("Zap")



       



   else :



       print("Invalid")





Num=int(input("enter the value of Num:"))

display(Num)
