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

def signIn(request):

    return render(request, "signIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
      user = authe.sign_in_with_email_and_password(email,passw)
    except:
      message = "Invalid Email Id or Password !! Please try again."
      return render(request, "signIn.html",{"messg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)  
    return render(request, "welcome.html",{"e":email})
def logout(request):
    auth.logout(request)
    return render(request, "signIn.html")