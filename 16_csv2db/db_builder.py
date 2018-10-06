#FattyPikachu (Derek Chan & Vincent Chi)
#SoftDev1 pd8
#K16 No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="curbur.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")    #create peeps table
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")    #create courses table

with open('data/peeps.csv') as csvfile: #opens the file for reading as a csvfile
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO peeps VALUES(" +
		"'" + row["name"] + "'"  +
		"," + row["age"] +
		"," + row["id"] + ")")

with open('data/courses.csv') as csvfile: #opens the file for reading as a csvfile
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES(" +
		"'" + row["code"] + "'" +
		"," + row["mark"] +
		"," + row["id"] + ")")

#==========================================================

db.commit() #save changes
db.close()  #close database