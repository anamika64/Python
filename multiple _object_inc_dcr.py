#Create a class Number with a private variable __num initialised through the constructor. Write methods increment, decrement and display. Create multiple objects from it.
                            
class Number():



    def __init__(self):

        self.__num = int(input("Enter the number"))



    def increment(self):

        self.__num += 1



    def decrement(self):

        self.__num -= 1



    def display(self):

        print(self.__num)







num1 = Number()



num2 = Number()



num1.increment()

num1.display()



num2.decrement()

num2.display()

