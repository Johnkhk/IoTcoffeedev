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


# CREATE NEWS TABLE
try:
  cursor.execute("""
    CREATE TABLE NEWS (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(50) NOT NULL,
      news  VARCHAR(500) NOT NULL,
      date  VARCHAR(50) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records into Users
query = "insert into NEWS (title, news, date) values (%s, %s, %s)"
values = [
  ('IoT Features','With the arrival of the Raspberry Pi 3, our team has developed MQTT functionality with the Pi through our website. Users can now reliably send data from the website to the coffeemaker.','May 22, 2020'),
  ('Website Developments','Newly implemented our dynamic news feed, which dynamically adds rows and fills in cells for each new news entry, giving our customers who have signed up a look at our product developments and other extra news relating to coffee. Also a product readiness indicator, showing our dynamic progress towards the final goal.','May 22, 2020'),
]
cursor.executemany(query, values)
db.commit()

# CREATE readiness TABLE
try:
  cursor.execute("""
    CREATE TABLE readiness (
      id integer  AUTO_INCREMENT PRIMARY KEY,
      metric VARCHAR(50) NOT NULL,
      descr  VARCHAR(500) NOT NULL,
      readiness  INT NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records into Users
query = "insert into readiness (metric, descr, readiness) values (%s, %s, %s)"
values = [
  ('Hardware','Our hardware prototype is fininshed and fully functional. Last measures include improving wire management and making the build more compact. Taste tests have been done and the metallic taste can be improved upon through more usage of the system.', 9),
  ('Website', 'Our website serves as not only a landing page where users can find out about the product and team and sign up for our newsletter, but also as an account login for accessing IoT features that the coffee maker uses.', 8),
  ('Firmware/Software', 'With MQTT as our network protocol, our website is able to send messages to the Raspberry Pi on our coffee maker. Last measures include setting up digital pins to work with the embedded firmware on our machine.', 7),
  ('Customer Acquisition Plan', 'After evaluating product/market fit and running tests on our MVP hypotheses, We have developed a clear idea of personas and clients. With a target demographic of young professionals, we plan to employ digital marketing and advertisements on forums and news websites, avenues where there is a more mature audience.', 8),
  ('Revenue Model', 'We expect to sell the coffee maker for $300. The COGS will be 66%, of which $150 will be from raw materials or prebuilt parts, and $50 will be from manufacturing and assembling. The subscription model comes from selling coffee pods to the customers. This will cost about $.50 per pod. Depending on the amount of pods the user needs the subscription will run from $15 to $30 per month.', 9)
]
cursor.executemany(query, values)
db.commit()


# Show Users Table
cursor.execute("select * from Users;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

cursor.execute("select * from cofset;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

cursor.execute("select * from accounts;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

db.close()

