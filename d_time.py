from datetime import date
d=date.today()
print("system date:",d)
print("only show curent year:",d.year)
print("only year :",d.strftime("%Y"))
print("only year :",d.strftime("%y"))
#month for month or strftime (%m)
print("only show month from current date:",d.month)# 10 means october
print("only show month from current date:",d.strftime("%m"))# 10 means october
print("only show month from current date:",d.strftime("%B"))#B return october
print("only show month from current date:",d.strftime("%b"))#b return oct

#for day
print("only show month from current date:",d.day)# 17 
print("only show month from current date:",d.strftime("%d"))# 17

#return weekday
print("only show month from current date:",d.strftime("%a"))# sat 
print("only show month from current date:",d.strftime("%A"))# saturday
print("only show month from current date:",d.strftime("%w"))# monday=1 tues=2 sat=6


