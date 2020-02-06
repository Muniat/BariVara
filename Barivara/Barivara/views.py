from django.shortcuts import render
from pyrebase import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyAdf_Ryf-EVfbBDHuATeHsVsRVS6DAqY6E",
    'authDomain': "barivara-8a196.firebaseapp.com",
    'databaseURL': "https://barivara-8a196.firebaseio.com",
    'projectId': "barivara-8a196",
    'storageBucket': "barivara-8a196.appspot.com",
    'messagingSenderId': "1076039240181",
    'appId': "1:1076039240181:web:aeb1676883189bdc3878bc",
    'measurementId': "G-E4J9W7LK03"
  }
  
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()

def signIn(request):

    return render(request, "LoginPage.html")

def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    try:
      user = authe.sign_in_with_email_and_password(email,password)
    except:
      message = "Invalid Email Id or Password! Please try again."
      return render(request, "LoginPage.html",{"message":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)  
    return render(request, "HomePage.html")
def logout(request):
    auth.logout(request)
    return render(request, "LoginPage.html")


def postsignup(request):  
    name=request.POST.get('name')
    number=request.POST.get('number')  #extra field
    email=request.POST.get('email')
    password=request.POST.get('pass')
    try:
      user=authe.create_user_with_email_and_password(email,password)
    except:
      message="Invalid Username/Email/Password! Please try again."
      return render(request, "LoginPage.html",{"message":message})

    uid = user['localId']

    data = {"name":name,"status":"1" , "Phone":number}
    #Trying to add number in the database, but its not working...
    database.child("users").child(uid).child("details").set(data)
    return render(request, "HomePage.html")