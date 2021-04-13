def info():

    fName = 'data.txt'

    a = open(fName, 'a')

    a.write(input('Enter your full name : ')+ ' : ' +input('Enter your number : ')+'\n')



def show():

    fName = 'data.txt'

    r = open(fName, 'r')

    print(r.read())



while True:

    print('1 : add information')

    print('2 : show data')

    print('3 : exit')



    ch = int(input('Enter choise'))



    if ch == 1:

        info()

    elif ch == 2:

        show()

    elif ch == 3:

        break

    else:

        print('error')

        
