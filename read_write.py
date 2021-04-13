#Create a class called FileManager with attributes filename. Add functions to read and write data into a file
class FileManager:

    filename = 'file1.txt'



    def read(self):

        r = open(self.filename,'r')

        print(r.read())



    def write(self):

        r = open(self.filename,'w')

        data = input('Enter what you want to add')

        r.write(data)





a = FileManager()



a.write()



a.read()
