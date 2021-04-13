#strong number using function



#Write a program to find the given number is strong number or not using function



def strongnumber(n):



    i=n#assigining value to variable i



    sum=0



    while(i>0):#condition



        y=i%10



        fact=1



        while(y>0):#codition for finding factorial



            fact=fact*y



            y=y-1



        sum=sum+fact



        i=i//10



    print("Sum:",sum)



    if(sum==n):



        return 1



    else:



        return 0



#Main program



n=int(input("Enter a number:"))



val=strongnumber(n)



if val==1:



    print("Strong number")



else:



    print("not a strong number")

