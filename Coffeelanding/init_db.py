# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']# different than inside the container and assumes default port of 3306

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

 # CREATED MOVES TABLE
try:
  cursor.execute("""
    CREATE TABLE accounts (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      username       VARCHAR(50) NOT NULL,
      password    VARCHAR(200) NOT NULL,
      validity       VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records into Moves
query = "insert into accounts (username, password, validity) values (%s, %s, %s)"
values = [
  ('john','john','valid'),
]
cursor.executemany(query, values)
db.commit()
# Create cofset Table

# CREATED USERS TABLE
try:
  cursor.execute("""
    CREATE TABLE Users (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      firstname  VARCHAR(50) NOT NULL,
      lastname   VARCHAR(50) NOT NULL,
      email       VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records into Users
query = "insert into Users (firstname, lastname, email) values (%s, %s, %s)"
values = [
  ('John','Ho','jawnho.hk@gmail.com'),
  ('Thuy','Hong','Nguyen'),
  
]
cursor.executemany(query, values)
db.commit()

try:
  cursor.execute("""
    CREATE TABLE cofset (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      coffeeid VARCHAR(50) NOT NULL,
      temperature VARCHAR(50) NOT NULL,
      time    VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records into cofset
query = "insert into cofset (coffeeid, temperature, time) values (%s, %s, %s)"
values = [
  ('someid', 'sometemp', 'sometime'), 
]
cursor.executemany(query, values)
db.commit()


# Show Users Table
#cursor.execute("select * from Users;")
#print('---------- DATABASE INITIALIZED ----------')
#[print(x) for x in cursor]

#cursor.execute("select * from cofset;")
#print('---------- DATABASE INITIALIZED ----------')
#[print(x) for x in cursor]

#cursor.execute("select * from accounts;")
#print('---------- DATABASE INITIALIZED ----------')
#[print(x) for x in cursor]

db.close()

