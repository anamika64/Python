import re

password=input("enter Password : ")

reg="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

#compiling regex
pat=re.compile(reg)

#searching regex
mat=re.search(pat,password)#mat user defined variable

#validation conditions
if(mat):
    print("Password is valid ")
else:
    print("password is invalid ")
    print("not less than 6 chars and greater than 20 chars and Atleast 1 small alphabets,1 capital alphabets ,1 special char(@$!%*#?&) and 1 digit(0-9)")
