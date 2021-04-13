bi=input("Enter binary number=>")
str = str()
sp1=bi.split(',')
for i in sp1:
    decimal= int(i ,2)
    if decimal%5==0:
        str.join(i)

print(str)
    
    
