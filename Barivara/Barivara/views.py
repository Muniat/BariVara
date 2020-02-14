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
    
    import datetime
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
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    #data = []

    #fetching data from the database
    #all_ad = database.child("users").child(a).child("advertisements").get()
    #for ad in all_ad.each():
        #adding each advertisement to the list 'data'
        #data.append(ad.val())
    timestamps = database.child('users').child(a).child('advertisements').shallow().get(idtoken).val()
    
    lis_time=[]
    

    for i in timestamps:
      lis_time.append(i)

    lis_time.sort(reverse=True)
    
    print(lis_time)

    advertisements = []

    for i in lis_time:
      adv = database.child('users').child(a).child('advertisements').child(i).child('address').get(idtoken).val()
      advertisements.append(adv)

    print(advertisements)

    date = []
    for i in lis_time:
      i = float(i)
      dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
      date.append(dat)

    print(date)  
    
    comb_lis = zip(lis_time,date,advertisements)
   
    return render(request, "HomePage.html", {'comb_lis':comb_lis})




def logout(request):
    auth.logout(request)
    return render(request, "LoginPage.html")

def postgooglelogin(request):
    return render(request, "HomePage.html")


def postsignup(request):  
    name=request.POST.get('name')
    number=request.POST.get('number')  
    email=request.POST.get('email')
    password=request.POST.get('pass')
    try:
      user=authe.create_user_with_email_and_password(email,password)
    except:
      message="Invalid Username/Email/Password! Please try again."
      return render(request, "LoginPage.html",{"message":message})
      
    uid = user['localId']

    data = {"name":name,"status":"1", "Phone":number}
    
    database.child("users").child(uid).child("details").set(data)
    return render(request, "LoginPage.html")

def create_advertisement(request):

    return render(request, "create_advertisement.html")

def create(request):

    import time
    from datetime import datetime, timezone
    import pytz
    tz = pytz.timezone('Asia/Dhaka')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    name=request.POST.get('name')
    number=request.POST.get('number')  
    address=request.POST.get('address')
    size=request.POST.get('size')
    fee=request.POST.get('fee')
    house_details=request.POST.get('house_details')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))


    data={"owner":name,"contact":number,"address":address,"size":size,"fee":fee,"house_details":house_details}
    database.child('users').child(a).child('advertisements').child(millis).set(data)
    return render(request, "HomePage.html")   


	
def your_advertisements(request):

    import datetime  
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child('users').child(a).child('advertisements').shallow().get(idtoken).val()
    
    lis_time=[]
    

    for i in timestamps:
      lis_time.append(i)

    lis_time.sort(reverse=True)
    
    print(lis_time)

    advertisements = []

    for i in lis_time:
      adv = database.child('users').child(a).child('advertisements').child(i).child('address').get(idtoken).val()
      advertisements.append(adv)

    print(advertisements)

    date = []
    for i in lis_time:
      i = float(i)
      dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
      date.append(dat)

    print(date)  
    
    comb_lis = zip(lis_time,date,advertisements)

    return render(request,'your_advertisements.html',{'comb_lis':comb_lis}) 

def advertisement_details(request):
   import datetime
   time=request.GET.get('z')
   idtoken = request.session['uid']
   a = authe.get_account_info(idtoken)
   a = a['users']
   a = a[0]
   a = a['localId']

   address= database.child('users').child(a).child('advertisements').child(time).child('address').get(idtoken).val()
   contact= database.child('users').child(a).child('advertisements').child(time).child('contact').get(idtoken).val()
   fee= database.child('users').child(a).child('advertisements').child(time).child('fee').get(idtoken).val()
   house_details= database.child('users').child(a).child('advertisements').child(time).child('house_details').get(idtoken).val()
   owner= database.child('users').child(a).child('advertisements').child(time).child('owner').get(idtoken).val()
   size= database.child('users').child(a).child('advertisements').child(time).child('size').get(idtoken).val()

   i=float(time)
   date=datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
   return render(request,"advertisement_details.html", {'a':address,'c':contact,'f':fee,'h':house_details,'o':owner,'s':size,'d':date})
  
  
def edit_advertisement(request):
   import datetime
   time=request.GET.get('z')
   idtoken = request.session['uid']
   a = authe.get_account_info(idtoken)
   a = a['users']
   a = a[0]
   a = a['localId']

   name=request.POST.get('name')
   number=request.POST.get('number')  
   address=request.POST.get('address')
   size=request.POST.get('size')
   fee=request.POST.get('fee')
   house_details=request.POST.get('house_details')

   i=float(time)
   date=datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
  
   data={"owner":name,"contact":number,"address":address,"size":size,"fee":fee,"house_details":house_details}
   database.child('users').child(a).child('advertisements').child(time).update(data)

   return render(request,'edit_advertisement.html')