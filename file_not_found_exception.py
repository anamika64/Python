                            
def read(name):

    try:

        r = open(name,'r')

        print(r.read())



    except FileNotFoundError:

        print('{} file is missing'.format(name))



read('anamika')
