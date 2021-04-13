employees = {}

def info(name, designation, salary):

    employees[name] = [designation, salary]



    try:

        if salary < 10000:

            raise Exception('LOW SALARY')



    except Exception as e:

        print(e)





info('anamika', 'engineer', 1000)

