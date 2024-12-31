import sqlite3

#Create SQLlite DB
connection= sqlite3.connect("Student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

# ## create the table
table_info="""
 create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
 SECTION VARCHAR(25),MARKS INT)

 """


cursor.execute(table_info)

# ## Insert some more records
cursor.execute('''Insert Into STUDENT values('ABC','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('XYZ','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Aklesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Mamta','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Chat','DEVOPS','A',35)''')
cursor.execute('''update STUDENT set name='Amit' where name ='Mukesh' ''')

## Display all the records
print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()


