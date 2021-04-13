filename = 'file.txt'



w = open(filename, 'w+')



w.write(input('Enter any text : '))



w.seek(0)



print(w.read())
