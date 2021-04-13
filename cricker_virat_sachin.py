#Create a class Cricketer with two objects virat and sachin. The class has two instance variables viz. name and birthyear. Create a method age which prints the current age of the cricketer. 

#Tip: Make use of datetime module to calculate the current year.
import datetime as dt

class  Cricketer():



    def __init__(self,name,birthyear):

        self.name = name

        self.birthyear = birthyear





    def age(self):

        return dt.datetime.now().year - self.birthyear





virat = Cricketer('Virat',1988)

sachin = Cricketer('Sachin',1973)





print(virat.age())

print(sachin.age())
