#Aleksandra Koroza, Vincent Chi: Chiroza
#SoftDev1 pd8
#K #17: Average  
#2018-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



DB_FILE="discobandit.db" #delete before every subsequent run

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# creates and populates table from csvfile with three specified columns
def createTable(filename,tblname,par1,par2,par3):
     with open(filename, newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          tblcommand = "CREATE TABLE {0}({1} TEXT, {2} INTEGER, {3} INTEGER)".format(tblname,par1,par2,par3)
          c.execute(tblcommand) #creates the table with specified parameters

          insertHdr = "INSERT INTO {0} ({1},{2},{3}) VALUES ".format(tblname,par1,par2,par3)
          for row in reader:
               insrtcommand = insertHdr + "('{0}','{1}','{2}')".format(row[par1],row[par2],row[par3])
               c.execute(insrtcommand)
               
# Looks up each student's grades, displays name, id and average           
def gradeLookup():
     cmd="select name, peeps.id, avg(mark) from peeps, courses where peeps.id=courses.id group by name"
     result= c.execute(cmd).fetchall() # now a list of tuples
     for tup in result:
          print("Name: {0}, ID: {1}, Average: {2}".format(tup[0],tup[1],tup[2]))
          
#create table of ids and associated averages          
def idTable(tblname):
     cmd="select peeps.id, avg(mark) from peeps, courses where peeps.id=courses.id group by name"
     result= c.execute(cmd).fetchall() # now a list of tuples
     tblcommand="CREATE TABLE {0}({1} INTEGER, {2} INTEGER)".format(tblname,"id","avg")
     c.execute(tblcommand) #table now exists to store id's and averages
     
     insertHdr = "INSERT INTO {0} ({1},{2}) VALUES ".format(tblname,"id","avg")
     for tup in result:
          insrtcommand = insertHdr + "('{0}','{1}')".format(tup[0],tup[1])
          c.execute(insrtcommand)
          
#create tables for peeps.csv
createTable('data/peeps.csv',"peeps","name","age","id")
#create table for courses.csv
createTable('data/courses.csv',"courses","code","mark","id")
gradeLookup()
idTable("peeps_avg")


#==========================================================

db.commit() #save changes
db.close()  #close database