#Create class Sports with an instance variables matches, player1score, player2score.Create a method match which increments the matches variable and randomly selects either player to win a match and add 6 points to his score.
#Create method result which declares the result after minimum 3 matches otherwise gives message to play more matches.
import random

class Sports():

    def __init__(self):#destructor

        self.player1 = input("Enter name of the player : ")

        self.player2 = input("Enter name of the player : ")

        self.matches = 0

        self.player1score = 0

        self.player2score = 0





    def match(self):

        self.matches += 1

        self.win = random.choice([self.player1, self.player2])

        

        if self.win == self.player1:

            self.player1score += 6



        else:

            self.player2score += 6





    def result(self):

        if self.matches % 3 == 0:

            print('Score of {} : {}'.format(self.player1,  self.player1score))

            print('Score of {} : {}'.format(self.player2,  self.player2score))

        else:

            print('Play more matches')





match1 = Sports()

while True:

    print('1 : Play')

    print('2 : Result')

    print('3 : Exit')

    ch = int(input('Enter your choice'))

    if ch == 1:

        match1.match()

    elif ch == 2:

        match1.result()

    else:

        break

