import sqlite3
try:
  #create a database connection to a SQLite database 
   sqlite_Connection = sqlite3.connect('ingenious.db')
   #creating a cursor object using the cursor method of the connection object
   conn = sqlite_Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   #executing a select statement
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   #method of the cursor object to fetch the data
   record = conn.fetchall()
   print("\nSQLite Database Version is: ", record)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
   #closing the database after completion
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")
