#to update the record of student table
#to change the city with mumbai
import pymysql
#step:to create connection string
#create the object of connect
servername="localhost"
username="root"
password=""
dbname="scl_mng"
try:
    con=pymysql.connect(servername,username,password,dbname)
except Exception:
    print("connection error")
else:
    print("connection successfully")

#step 2: create cursor
#create object of cursor  cur cursor() inbuilt method of connect class
cur=con.cursor()

#step 3:query fire on table
en=int(input("enter enroll no be deleted  : "))
query="delete from student where enroll=%s"#%s string unknown

#query run,use execute method , this inbuilt method of cursor
try:
    cur.execute(query,en)
except Exception:
    print("query error")
else:
    print("record detele successfully")

#step  4:
con.commit() #to change permanentlt in table
cur.close()#close inbuilt
con.close()#close inbuilt method of connect
