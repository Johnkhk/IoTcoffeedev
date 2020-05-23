from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import json
import mysql.connector as mysql
import os
import requests
import time
import paho.mqtt.client as mqtt


                ##############################################################################
                #                 Including completed code from assignment API
                ##############################################################################
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_readiness(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT JSON_ARRAYAGG(JSON_OBJECT('metric', metric, 'descr', descr, 'readiness', readiness)) from readiness;")
  records = cursor.fetchall()
  print("BOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMM")
  print(records, type(records))
  #print(json.dumps(records), type(json.dumps(records)))
  pp=json.dumps(records)
  print(pp, type(pp))
  #print(json.loads())
  #pf = pp[2:len(pp)-2]
  #print(pf)
  ff = pp[2:len(pp)-2]
  print(ff)
  fy = json.loads(ff)
  print(fy)
  y = {fy}
  print(y)
  print("BOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMMBOOOOOOOOMMMMM")
  response = Response(body=fy)
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response

def get_news(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT JSON_ARRAYAGG(JSON_OBJECT('title', title, 'news', news, 'date', date)) from NEWS;")
  records = cursor.fetchall()
  print("HAHAHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAH")
  print(records, type(records))
  #print(json.dumps(records), type(json.dumps(records)))
  pp=json.dumps(records)
  print(pp, type(pp))
  #print(json.loads())
  #pf = pp[2:len(pp)-2]
  #print(pf)
  ff = pp[2:len(pp)-2]
  print(ff)
  fy = json.loads(ff)
  print(fy)
  y = {fy}
  print(y)
  print("HAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAH")
  response = Response(body=fy)
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response

def get_numusers(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT count(*) from Users;")
  records = cursor.fetchall()
  print("WOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOWWOWOWOWOWOWOW")
  print(records)
  
  #records = records[2:len(records)-2]
  #print(json.dumps(records))
  #print(json.loads(records))
  ff = json.dumps(records)
  pf = ff[2:len(ff)-2]
  print(ff)
  print(pf)
  x = json.loads(pf)
  y = {"numusers": x}
  print(x)
  print(y)
  response = Response(body=json.dumps(y))
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response
  #response.headers.update({'Access-Control-Allow-Origin': '*'})
  #self.send_header("Access-Control-Allow-Origin", "*")
  #return y
  #return json.dumps({"AVG(age)": str(array[0])})


def get_students_method(req):
  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT first_name, last_name, course_name,count(course_id) from Users user, Courses course, Enrollments enroll where user.id=course.prof_id and course.id=enroll.course_id group by course_id;")
  records = cursor.fetchall()
  return json.dumps(records)

def get_student_method(req):
  # Retrieve the route argument (this is not GET/POST data!)
  the_id = req.matchdict['course_id']

  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT first_name, last_name FROM Users JOIN Enrollments on student_id=Users.id and course_id='%s';" % the_id)
  record = cursor.fetchall()
  db.close()

  if record is None:
    return ""

  return json.dumps(record)


def total_users(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select count(id) from Users;")
  record = cursor.fetchall()
  db.close()
  return json.dumps(record)

def average_age(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select AVG(age) from Users;")
  record = cursor.fetchall()
  for x in record:
      array = x
  db.close()
  return json.dumps({"AVG(age)": str(array[0])})
  
def user_in_course(req):

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select count(course_id) from Enrollments group by course_id;")
  record = cursor.fetchall()
  db.close()
  r1= record[0]
  r2= record[1]
  response = {
      "ECE140": r1[0],
      "ECE141": r2[0]
  }
  return json.dumps(response)

                ##############################################################################
                #                         ---- End of added code ----                        #
                ##############################################################################


################DB CONVERSION####################
def get_users_db(req): 
  print("========================================================")

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  print("========================================================")

  cursor.execute("SELECT Username, Status from Users;")
  records = cursor.fetchall()
  value_to_return = {}
  value_2_return = {}
  answer = "["
  for values in records:
    value_2_return['Username'] = values[0]
    value_2_return['Status'] = values[1]
    temp = str(value_2_return)
    answer += temp
    answer += ","
    print(answer)
  answer = answer[0:len(answer)-1]
  answer += "]"
  print(answer)
  value_to_return = eval(answer)
  return value_to_return

def get_users(req):
  try:
    # Open the file to read (assuming it exists)
    with open('users.txt', 'r') as user_files:
      user_logs = json.load(user_files)
      user_files.close()
      return user_logs
  except FileNotFoundError:
    # Create file if it does not exist
    user_files = open('users.txt', 'a+')
    user_files.close()
    return EnvironmentError

################DB CONVERSION####################
def newac(req):
  # View the Dictionary that was Posted
  # Get the fname
  newPsw = str(req.params.getall("username"))
  # Get rid of the [] that comes from req
  newPsw = newPsw[2:len(newPsw)-2]
  # Get the last name the user entered
  newName = str(req.params.getall("password"))
  # Get rid of the [] that comes from req
  newName = newName[2:len(newName)-2]
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # Insert Records
  query = "insert into accounts (username, password, validity) values (%s, %s, %s)"
  values = [
  (newName,newPsw, "valid"),
  ]
  cursor.executemany(query, values)
  db.commit()
  cursor.execute("SELECT username, password from accounts;")
  records = cursor.fetchall()
  return json.dumps(records)
def add_users_db(req):
  # View the Dictionary that was Posted
  # Get the fname
  newPsw = str(req.params.getall("firstname"))
  # Get rid of the [] that comes from req
  newPsw = newPsw[2:len(newPsw)-2]
  # Get the last name the user entered
  newName = str(req.params.getall("lastname"))
  # Get rid of the [] that comes from req
  newName = newName[2:len(newName)-2]
  #Get the email
  email = str(req.params.getall("email"))
  # Get rid of the [] that comes from req
  email = email[2:len(email)-2]
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # Insert Records
  query = "insert into Users (firstname, lastname, email) values (%s, %s, %s)"
  values = [
  (newName,newPsw,email),
  ]
  cursor.executemany(query, values)
  db.commit()
  cursor.execute("SELECT firstname, lastname, email from Users;")
  records = cursor.fetchall()
  return json.dumps(records)

def coffeeset(req):
  # View the Dictionary that was Posted
  # Get the fname
  print("bbbeeeeeppppp")
  temp = str(req.params.getall("temperature"))
  date = str(req.params.getall("date"))
  time = str(req.params.getall("time"))
  recur = str(req.params.getall("recur"))
  # Get rid of the [] that comes from req
  temp = temp[2:len(temp)-2]
  date = date[2:len(date)-2]
  time = time[2:len(time)-2]
  recur = recur[2:len(recur)-2]
  msg ='{"temperature": "'+temp+'", "date": "' +date+ '", "time": "'+time+'", "recur": "'+recur+'"}'
  print(msg)
  # SEND TO RASPBERRY PI WITH MQTT
  client = mqtt.Client("JJJ")
  client.connect("64.227.101.67", port=1883, keepalive=60, bind_address="")
  client.publish("test", msg)

  #SEND TO DATABASE
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # Insert Records
  query = "insert into cofset (coffeeid, temperature, time) values (%s, %s, %s)"
  values = [
  ("testid", temp, time),
  ]
  print("GOT THIS FAR1")
  cursor.executemany(query, values)
  db.commit()
  print("GOT THIS FAR2")
  cursor.execute("SELECT coffeeid, temperature, time from cofset;")
  records = cursor.fetchall()
  print(records)
  return json.dumps(records)

def add_users(req):
  # View the Dictionary that was Posted
  # Get the Password
  newPsw = str(req.params.getall("Password"))
  # Get rid of the [] that comes from req
  newPsw = newPsw[2:len(newPsw)-2]
  print(newPsw)
  # Get the name the user entered
  newName = str(req.params.getall("Username"))
  # Get rid of the [] that comes from req
  newName = newName[2:len(newName)-2]
  print(newName)

  # This will append user information to json
  user_info = {"Username": newName, "Password": newPsw, "Status": "Pending"}
  try:
    # Open the file to read from it
    with open('users.txt', 'r') as user_files:
      try:
        # Load the json file
        user_logs2 = json.load(user_files)
      except json.decoder.JSONDecodeError:
        # If an error occurs, close the file
        user_files.close()
        # Open file to write to it the first time
        with open('users.txt', 'w+') as user_files:
         user_logs2 = [user_info]
         json.dump(user_logs2, user_files)
         user_files.close()
         return user_logs2
      user_files.close()
    with open('users.txt', 'w+') as user_files:
      user_logs2.append(user_info)
      json.dump(user_logs2, user_files)
      user_files.close()

      return user_logs2
  except:
    return Exception


################DB CONVERSION####################
def check_password_db(req):
  newPsw = str(req.params.getall("password"))
  newPsw = newPsw[2:len(newPsw)-2]
  newName = str(req.params.getall("username"))
  newName = newName[2:len(newName)-2]
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  cursor.execute("SELECT username from accounts WHERE username='%s';" % newName)
  userResult = cursor.fetchall()
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  cursor.execute("SELECT password from accounts WHERE password='%s';" % newPsw)
  passwordResult = cursor.fetchall()
  passwordResult = str(passwordResult)
  passwordResult = passwordResult[3:len(newPsw)+3]
  userResult = str(userResult)
  userResult = userResult[3:len(newName)+3]
  print(userResult)
  if newName == userResult:
    if passwordResult == newPsw:
     return True
  return False
  
def check_password(req):
  newPsw = str(req.params.getall("Password"))
  newPsw = newPsw[2:len(newPsw)-2]

  newName = str(req.params.getall("Username"))
  newName = newName[2:len(newName)-2]

  try:
    with open('users.txt', 'r') as user_files:
      user_logs = json.load(user_files)
      for logs in user_logs:
        if logs["Username"] == newName:
          if logs["Password"] == newPsw:
            user_files.close()
            return True
          else:
            user_files.close()
            return False
      return False
  except FileNotFoundError:
    return False

################DB CONVERSION####################
def validity_db(req):
  newName = str(req.params.getall("username"))
  newName = newName[2:len(newName)-2]
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  cursor.execute("SELECT validity from accounts WHERE username='%s';" % newName)
  validityResult = cursor.fetchall()
  validityResult = str(validityResult)
  validityResult = validityResult[3:8]
  print(validityResult)
  print(str(validityResult) == "valid")
  if str(validityResult) == "valid":
    return True
  return False
  
def validity(req):
  newName = str(req.params.getall("Username"))
  newName = newName[2:len(newName)-2]

  try:
    with open('users.txt', 'r') as user_files:
      user_logs = json.load(user_files)
      for logs in user_logs:
        if logs["Username"] == newName:
          if logs["Status"] == "Valid":
            return True
          else:
            user_files.close()
            return False
      return False
  except FileNotFoundError:
    return False

  
################DB CONVERSION####################
def change_status_db(req):
  # Store the json body
  info = req.json_body
  # Create a response (will not be sent due to CORS issue)
  response = {}
  response['success'] = True
  # this Response object allows us to set a header so that CORS requests can be handled... this should really be behind OAUTH
  response = Response(body=json.dumps(response))
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  # Extract the Username
  usrChanged = info["Username"]
  # Extract the new Status
  newStatus = info['Status']
  #connect to database
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("Update Users SET Status = '%s' WHERE Username='%s';" %(newStatus,usrChanged))
  print(newStatus)
  print(usrChanged)
  db.commit()
  return response


def change_status(req):
  # Store the json body
  info = req.json_body

  # Create a response (will not be sent due to CORS issue)
  response = {}
  response['success'] = True
  # this Response object allows us to set a header so that CORS requests can be handled... this should really be behind OAUTH
  response = Response(body=json.dumps(response))
  response.headers.update({'Access-Control-Allow-Origin': '*',})

  # Extract the Username
  usrChanged = info["Username"]
  # Extract the new Status
  newStatus = info['Status']

  try:
    # Open the file to read from it
    with open('users.txt', 'r') as user_files:
      try:
        # Load the json file
        user_logs2 = json.load(user_files)
      except json.decoder.JSONDecodeError:
        # If an error occurs, close the file
        user_files.close()
      user_files.close()
    with open('users.txt', 'w+') as user_files:
      for user in user_logs2:
        if usrChanged == user["Username"]:
          user["Status"] = newStatus
          json.dump(user_logs2, user_files)
          user_files.close()
      print("SUCCESS: Changes were made")
      return response
  except:
    return False


###THIS UPDATES STATUS IN MOVES TO COMPLETED, GIVEN A CERTAIN ROW
def receive_moves(req):

  
  req = str(req.body)
  print("Receiveing moves: ", req)
  rowNumber = req[5:len(req)-1]


  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("Update Moves SET status='%s' WHERE id='%s';" %("Completed",rowNumber))
  db.commit()

  response = {}
  response['Success'] = True
  response_as_string = json.dumps(response)
  return response_as_string

def requested_moves(req):

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()

  cursor.execute("SELECT moveId,startTime,direction,userId,status from Moves;")
  records = cursor.fetchall()
  answer = "["
  value_to_return = {}
  value_2_return = {}
  for values in records:
    value_2_return['moveId'] = values[0]
    value_2_return['startTime'] = values[1]
    value_2_return['direction'] = values[2]
    value_2_return['userId'] = values[3]
    value_2_return['status'] = values[4]
    temp = str(value_2_return)
    answer += temp
    answer += ","
    #print(answer)
  answer = answer[0:len(answer)-1]
  answer += "]"
  #print(answer)
  value_to_return = eval(answer)
  response = Response(body=json.dumps(value_to_return))
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response

def sent_moves(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT * FROM (SELECT * FROM Moves ORDER BY ID DESC LIMIT 2) TMP ORDER BY TMP.ID ASC;")
  #cursor.execute("SELECT moveId,startTime,direction,userId,status from Moves;")

  records = cursor.fetchall()
  answer = "["
  value_to_return = {}
  value_2_return = {}
  for values in records:
    value_2_return['moveId'] = values[0]
    value_2_return['startTime'] = values[2]
    value_2_return['direction'] = values[3]
    value_2_return['userId'] = values[4]
    value_2_return['status'] = values[5]
    temp = str(value_2_return)
    answer += temp
    answer += ","

  answer = answer[0:len(answer)-1]
  answer += "]"
  value_to_return = eval(answer)
  print("from the database:", value_to_return)
  return value_to_return

def send_moves(req):
  newMove = req.json_body
  print(newMove)
  print("1-----------------------")
  a = newMove["moveID"]
  b = newMove["startTime"]
  c = newMove["direction"]
  d = newMove["userId"]
  e = newMove["status"]
  print("2---------------------------------------------")


  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  print("3---------------------------------------------")
  query = "INSERT INTO Moves (moveId, startTime, direction, userId, status) values (%s, %s, %s, %s, %s);"
  values = (a,b,c,d,e)
  print("4---------------------------------------------")
  cursor.execute(query, values)
  print("5---------------------------------------------")

  db.commit()

  response = {}
  response['success'] = True
  # this Response object allows us to set a header so that CORS requests can be handled... this should really be behind OAUTH
  response = Response(body=json.dumps(response))
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response

if __name__ == '__main__':
  config = Configurator()

 ##########CHANGE get_users method to get_users_db when ready to switch completely to database!!!!
  config.add_route('users_route', '/users')
  config.add_view(get_users_db, route_name='users_route', renderer='json')

 ##########CHANGE add_users method to add_users_db when ready to switch completely to database!!!!
  config.add_route('add_new_user', '/new_users')
  config.add_view(add_users_db, route_name='add_new_user', renderer='json')

  config.add_route('coffeeset', '/coffeeset')
  config.add_view(coffeeset, route_name='coffeeset', renderer='json')

 ##########CHANGE check_password method to check_password_db when ready to switch completely to database!!!!
  config.add_route('check_validity', '/check_password')
  config.add_view(check_password_db, route_name='check_validity', renderer='json')

 ##########CHANGE validity method to validity_db when ready to switch completely to database!!!!
  config.add_route('validity', '/check_validity')
  config.add_view(validity_db, route_name='validity', renderer='json')

  ##########CHANGE change_status method to change_status_db when ready to switch completely to database!!!!
  config.add_route('change_status', '/change_the_status', request_method="POST")
  config.add_view(change_status_db, route_name='change_status', renderer='json')

  # route added for controller posting moves
  config.add_route('move', '/receive_moves', request_method="POST")
  config.add_view(receive_moves, route_name='move', renderer = 'json')
  # note: *** on the browser connect to: http://192.168.1.93:5001/receive_moves to see this get executed

  config.add_route('req_move', '/requested_moves')
  config.add_view(requested_moves, route_name='req_move', renderer = 'json')

  config.add_route('send_moves', '/send_moves', request_method="POST")
  config.add_view(send_moves, route_name='send_moves', renderer = 'json')

  config.add_route('sent_moves_to_jetbot', '/sent_moves_to_jetbot') #route added for controller posting moves
  config.add_view(sent_moves, route_name='sent_moves_to_jetbot', renderer="json")


              ##############################################################################
              #                        Adding Routes to Database                           #
              ##############################################################################

  config.add_route('get_numusers', '/get_numusers')
  config.add_view(get_numusers, route_name='get_numusers', renderer='json')

  config.add_route('get_students', '/students')
  config.add_view(get_students_method, route_name='get_students', renderer='json')

  config.add_route('get_student', '/student/{course_id}')
  config.add_view(get_student_method, route_name='get_student', renderer='json')

  config.add_route('total', '/users/count')
  config.add_view(total_users, route_name='total', renderer='json')

  config.add_route('avg_age', '/users/age')
  config.add_view(average_age, route_name='avg_age', renderer='json')

  config.add_route('course', '/courses/users')
  config.add_view(user_in_course, route_name='course', renderer='json')

  config.add_route('newac', '/newac')
  config.add_view(newac, route_name='newac', renderer='json')

  config.add_route('get_news', '/get_news')
  config.add_view(get_news, route_name='get_news', renderer='json')

  config.add_route('get_readiness', '/get_readiness')
  config.add_view(get_readiness, route_name='get_readiness', renderer='json')

              ##############################################################################
              #                        --END OF CODE ---                                   #
              ##############################################################################
  

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 5000, app)
  server.serve_forever()
