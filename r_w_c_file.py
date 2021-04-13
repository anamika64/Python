
class FileHandling():



    def __init__(self):

        self.fName = input('Enter file name :')+'.txt'

        self.r = open(self.fName, 'w+')



    def write(self):

        self.r.write(input('Enter any text'))



    def read(self):

        self.r.seek(0)

        print(self.r.read())



    def close(self):

        self.r.close()



file1 = FileHandling()

file1.write()

file1.read()

file1.close()

