from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import json
import requests
import os

REST_SERVER = os.environ['REST_SERVER']


# Show all the users in the database
def show_users(req):
  # "/users" comes from the route defined in rest_server.py
  Users = requests.get(REST_SERVER + "/users").json()
  # The word "users" is a variable that is used in the show_users.html
  return render_to_response('templates/show_users.html', {'users': Users}, request=req)


def add_new_user(req):
  # Get all the data that is going to be sent (needs to be a dict like "data")
  # print(req.params) #debugging
  data = {"firstname": req.params['firstname'], "lastname":  req.params['lastname'], "email":  req.params['email'],}
  New_user = requests.post(REST_SERVER + '/new_users', data=data).json()
  return render_to_response('templates/metrics.html', {}, request=req)

def newac(req):
  #UserName = str(req.params.getall("usename"))
  #UserName = UserName[2:len(newName)-2]
  #PassWord = str(req.params.getall("password"))
  #PassWord = PassWord[2:len(newName)-2]
  #if(len(UserName<9 or PassWord<9)
  #  return(login(req))
  data={"username": req.params['username'], "password": req.params['password'],}
  Newac = requests.post(REST_SERVER + '/newac', data=data).json()
  return render_to_response('templates/login.html', {}, request=req)

def setcoffeex(req):
  print("BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  temperature=req.params["temperature"]
  print(temperature)
  date=req.params["date"]
  print(date)
  time=req.params["time"]
  print(time)
  recur=req.params["recur"]
  print(recur)

 
  data = {"temperature": temperature, "date": date, "time": time, "recur": recur}
  print("rannnnn2")
  print(data)

  coffeetemp = requests.post(REST_SERVER + '/coffeeset', data=data).json()
  print("whatalifemann")
  return render_to_response('templates/timer.html', {}, request=req)

# This function will become useless
def changestatus(req):
  # Get all the data that is going to be sent (needs to be a dict like "data")
  # current does not run since all info is being sent to the Rest server
  print("1 *****************************************************")
  print(req.json_body)
  info_to_send = req.json_body
  print("2 *****************************************************")
  print(info_to_send)

 # data = {"Username": info_to_send['Username'],
  #        "Status": info_to_send['Status']}
  #newstatus = requests.post(REST_SERVER + '/change_status', data = data).json()
  return render_to_response('templates/did_log_in.html', {}, request =req)
  #return True



# Compare credentials from request (from user) to json
def correct_password(req):
  data = {"username": req.params['username'], "password":  req.params['password']}
  validity = requests.post(REST_SERVER + '/check_password', data = data).json()
  return validity

def valid_user(req):
  try:
    data = {"username": req.params['username']}
  except:
    data = req
  validity = requests.post(REST_SERVER + '/check_validity', data = data).json()
  return validity

# Route to validate login credentials...
def post_login(req):
  if valid_user(req) and correct_password(req):
    return menuportal(req)#controller(req)#
  else:
    return render_to_response('templates/did_log_in.html', {'tag': 'Incorrect Password'}, request = req)

def loginx(req):
  if valid_user(req) and correct_password(req):
    return setcoffee(req)#controller(req)#
  else:
    return render_to_response('templates/login.html', {'tag': 'Incorrect Password'}, request = req)

# These currently just render the html files 
def sign_up(req):
  return render_to_response('templates/sign_up.html', {}, request =req)

def product(req):
  return render_to_response('templates/product.html', {}, request =req)

def pricing(req):
  return render_to_response('templates/pricing.html', {}, request =req)

def setcoffee(req):
  return render_to_response('templates/setter.html', {'username': req.params['username']}, request =req)

#def getboi(req):
 # numusers = requests.get(REST_SERVER + "/get_numusers").json()
  #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  ##p#rint(numusers)
  #print(type(numusers))
  #print(json.dumps(numusers))
  #return render_to_response('templates/metrics.html', {"numuser": numusers}, request =req)
  
  #print(JSON.parse(numusers))
  #x=JSON.parse(numusers)
  #print(json.parse(numu))
  #print(req.params['numusers'])
  #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  #return numusers#json.dumps(numusers) #{'numusers': req.params['numusers']}

def metrics(req):
  print("AGGAGAGAGG")
  numnews = requests.get(REST_SERVER + "/get_news").json()
  nummetrics = requests.get(REST_SERVER + "/get_readiness").json()
  print("AGGAGAGAGG")
  print(numnews)
  print(len(numnews))
  return render_to_response('templates/metrics.html', {'length':numnews, 'lengthg':nummetrics}, request =req)

  #return render_to_response('templates/metrics.html', {}, request =req, {'numusers': numusers}, request =req)

def about(req):
  return render_to_response('templates/about.html', {}, request =req)

def portal(req):
  return render_to_response('templates/index.html', {}, request =req)

def signup_ac(req):
  return render_to_response('templates/signup_ac.html', {}, request =req)
 
#def login(req):
  #return render_to_response('templates/did_log_in.html', {}, request =req)
def login(req):
  return render_to_response('templates/login.html', {}, request =req)


def admin(req):
  Users = requests.get(REST_SERVER + "/users").json()
  return render_to_response('templates/adminportal.html',{'users': Users}, request =req)

def tracker(req):
  moves = requests.get(REST_SERVER + "/requested_moves").json()
  return render_to_response('templates/tracker.html', {'Username': req.params['Username'], 'moves': moves}, request =req)
 
def controller(req):
  return render_to_response('templates/controller.html', {'Username': req.params['Username']}, request =req)

def menuportal(req):
  return render_to_response('templates/menuportal.html', {'Username': req.params['Username']}, request =req)

def post_menu(req):
  data = {"nextLocation":  req.params['input'], "Username": req.params['Username']}
  if valid_user(data):
    if data['nextLocation'] == 'Tracker':
      return tracker(req)
    if data['nextLocation'] == 'Controller':
      return controller(req)
    if data['nextLocation'] == 'admin':
      return admin(req)

  return render_to_response('templates/did_log_in.html', {}, request =req)

########################################################################################
#                                Main Function
########################################################################################
if __name__ == '__main__':

  config = Configurator()
  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  # This is the "MAIN" page localhost:50000
  # Adds a route v2 so you can have localhost:5000/ or localhost:5000/v2
  config.add_route('v2', '/')
  # Loading stuff from the server
  config.add_view(portal, route_name='v2') #change to controller

  config.add_route('show_users', '/show_users')
  config.add_view(show_users, route_name='show_users')  

  config.add_route('changestatus', '/change_status')
  #config.add_view(changestatus, route_name='changestatus')
  config.add_view(changestatus, route_name='changestatus', request_method = "POST")

  config.add_route('new_user', '/new_user')
  #For view users(quick debugging)
  #config.add_view(show_users, route_name='new_user')
  # What send info over to the Rest Server
  config.add_view(add_new_user, route_name='new_user', request_method = "POST")

  config.add_route('setcoffeex', '/setcoffeex')
  config.add_view(setcoffeex, route_name='setcoffeex', request_method = "POST")

  config.add_route('about', '/about')
  config.add_view(about, route_name='about')
  
  config.add_route('sign_up', '/sign_up')
  config.add_view(sign_up, route_name='sign_up')
  

  config.add_route('login', '/login')
  config.add_view(login, route_name='login')
 
  config.add_route('post_login', '/post_login')
  config.add_view(post_login, route_name='post_login', request_method = "POST")
  
  config.add_route('tracker', '/tracker') # Added route for tracker 
  config.add_view(tracker, route_name='tracker')
  
  config.add_route('menuportal', '/menuportal') # Added route for menuportal
  config.add_view(menuportal, route_name='menuportal')

  config.add_route('post_menu', '/post_menu')
  config.add_view(post_menu, route_name='post_menu', request_method = "POST")

  config.add_route('setcoffee', '/setcoffee')
  config.add_view(setcoffee, route_name='setcoffee')

  config.add_route('product', '/product')
  config.add_view(product, route_name='product')

  config.add_route('pricing', '/pricing')
  config.add_view(pricing, route_name='pricing')

  config.add_route('loginx', '/loginx')
  config.add_view(loginx, route_name='loginx')

  config.add_route('signup_ac', '/signup_ac')
  config.add_view(signup_ac, route_name='signup_ac')

  config.add_route('newac', '/newac')
  config.add_view(newac, route_name='newac')

  config.add_route('metrics', '/metrics')
  config.add_view(metrics, route_name='metrics')

  #config.add_route('getboi', '/getboi')
  #config.add_view(getboi, route_name='getboi')
  
  config.add_static_view(name='/', path = './public', cache_max_age = 3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 5000, app)
  server.serve_forever()
