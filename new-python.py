#!/usr/bin/python3
import pymysql
'''x=print('do you want to create a database? If yes,enter y. if you want to use an existing database, enter n')
if x=='y' or x=='Y':
    db1=input('enter database name')
    db.pymysql.connect(host='localhost',user='root',password="")
    cur=db.cursor()
    cur.execute('create database'+db1)
    print('database created')
else:
    db2=input('enter database name')
    db=pymysql.connect(host='localhost',user='root',password="",db = '+db2+')
    print('connected successfully')'''

db1=input('enter database name ')
db=pymysql.connect(host='localhost',user='root',password='root')
cur=db.cursor()
cur.execute('create database'+db1)
print('database created')
