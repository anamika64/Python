#INSER RECORD INTO TABLE
import pymysql
#STEP 1#create connection string python with mysqlserver
servername="localhost"
username="root"
password=""
dbname="country_name" #dbname means database name
try:
    con=pymysql.connect(servername,username,password,dbname) #con user defined object name

except Exception:
    print("Connection Error")
else:
    print("Connection successfully")


#STEP 2 CURSOR CREATION
#create the cursor using the inbuilt method cursor()

cur=con.cursor() #create the cursor cur (connect table from connection string con)
#input from user on output screen on runtime
i=int(input("enter id:"))
n=input("enter the country name:")
r=int(input("enter the rank: "))




#step 3: Query Fire
#here to insert record in table : DML
query="INSERT INTO country(id,name,rank)VALUES(%s,%s,%s)"

#tuple variable: val
val=(i,n,r)

#step4 Query run with the help of execute(), it is inbuilt method of cursor class
try:
    cur.execute(query,val)
except Exception:
    print("Query error")
else:
    con.commit()
    #commit() inbuilt method of commit()
    print("Record save sucessfully")
cur.close()
con.close()
