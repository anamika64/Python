class Number():

    def __init__(self,num):

        self.num = num



    def __mul__(self,other):

        return self.num * other.num







num1 = Number(12)

num2 = Number(2)





num3 = num1 * num2



print(num3)

