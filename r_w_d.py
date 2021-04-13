import os

import shutil

def read(fname):

    r = open(fname, 'r')

    print(r.read())



def write(fname):

    r = open(fname, 'w')

    data = input('Enter any text :')

    r.write(data)



def delete(fname):

    os.remove(fname)



def rename(fname):

    new = input('Enter new name for file :')

    name = new + '.txt'

    source = 'F:/Data Science/File Operator/'+fname

    dest = 'F:/Data Science/File Operator/'+name

    os.rename(source, dest) 



def copy(fname):

    new = input('Enter new file name')

    name = new +'.txt'

    source = 'F:/Data Science/File Operator/' + fname

    dest = 'F:/Data Science/File Operator/'+name

    os.rename(source, dest)









filename = input('Enter file name :')+'.txt'



while True:

    print('1: read')

    print('2: write')

    print('3: delete')

    print('4: rename')

    print('5: copy')

    print('6: exit')



    ch = int(input('choise :'))



    if ch == 1:

        read(filename)

    elif ch == 2:

        write(filename)

    elif ch == 3:

        delete(filename)

    elif ch == 4:

        rename(filename)

    elif ch == 5:

        copy(filename)

    elif ch == 6:

        break

    else:

        print('Error')

    
