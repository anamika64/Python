#Add InvalidPinError and InsufficientBalanceError in netbanking application
usernames = {}

log = False





class Bank:





    def __init__(self,number,name,userName,passwd):

        """

        object of class bank is created here with number, name, username and password

        """

        self.number = number

        self.name = name

        self.userName = userName

        self.passwd = passwd

        self.balence = 0

        usernames[self.userName] = [self.passwd,self.number,self.name,self.balence]

        print('Account created')

        print(usernames)





    def login(self):

        """

        Method for logging in

        """

        global log

        self.userName = input("Enter your username")

        self.passwd = input("Enter your Password")

        if self.userName in usernames:

            if self.passwd in usernames[self.userName]:

                log = True

                print('logged in')

        else:

            print("Username is Incorrect")





    def checkBalence(self):

        global log

        if log == True:

            print(usernames[self.userName][3])





    def addMoney(self):

        global log

        if log == True:

            add = float(input("How much money you want to add to your account"))

            usernames[self.userName][3] = usernames[self.userName][3] + add





    def transfer(self):

        global log

        if log == True:

            user = input('Enter username where you want to transfer amount')

            amount = float(input('How much money you want to transfer'))

            try:

                if usernames[self.userName][3]-amount <= 0:

                    raise Exception('Insufficiant balence')

                else:

                    usernames[self.userName][3] = usernames[self.userName][3] - amount

                    usernames[user][3] += amount

            except Exception as e:

                print(e)





def main(): 

    while True:

        print("1. Register new account to bank")

        print("2. Login to account")

        print("3. Exit")

        ch=int(input("Enter Choice => "))

        if ch==1:

            global name

            number = int(input('Enter your mobile number : '))

            name = input('Enter your name : ')

            userName = input('Enter a username : ')

            passwd = input('Enter password : ')



            name = Bank(number,name,userName,passwd)

        elif ch==2:

            name.login()

            try:

                if log == True:   

                    while True:

                        print("1. Check your balence")

                        print("2. Add money to account")

                        print("3. Transfer money to other account")

                        print("4. Exit")

                        ch = int(input('Enter your choise'))

                        if ch == 1:

                            name.checkBalence()

                        elif ch == 2:

                            name.addMoney()

                        elif ch == 3:

                            name.transfer()

                        elif ch == 4:

                            break

                        else:

                            print("Try again....!")

                else:

                    raise Exception('Incorrect PIN')

            except Exception as e:

                print(e)

        elif ch == 3:

            break

        else:

            print("Try again....!")

            

main()


          
