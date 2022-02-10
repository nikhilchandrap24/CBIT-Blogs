from django import forms
from django.contrib import auth,messages
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, render
from . models import BlogData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('writeblog')
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST['current']
        user= request.user
        if user.check_password(current_password):
            
            new_password = request.POST['new']
            user.set_password(new_password)
            user.save()  
            return render(request,'changepassword.html',{'msg':"Password changed successfully!"})
        else:
            print(user.password,current_password)
            return render(request,'changepassword.html',{'msg':"Please check your current password and try again!"})
    else:
        return render(request,'changepassword.html')
def success(request):
    if request.method == "POST":
        name = request.POST["names"]
        roll_number = request.POST["roll"]
        email=request.POST["email"]
        password=request.POST["password"]
        regx = "ugs"
        if not'ugs' in email and not '@cbit' in email :
            return render(request,'success.html',{'msg':"Please check your Email ID. Make sure you enter your official college email ID only. ",'key':False})
        confirm_password = request.POST['confirm_password']
        if(password!=confirm_password):
            return render(request,'success.html',{'msg':"Passwords do not match...",'key':False})
        try:
            user = User.objects.create_user(username = roll_number,first_name = name,password = password, email=email,is_superuser = False)
            user.save()
            return render(request,'success.html',{'msg':"Account created successfully...",'key':True})
        except:
            return render(request,'success.html',{'msg':"User Already Exists ..",'key':False})
    else:
        return render(request,'success.html')

def logout(request):
    auth.logout(request)
    return redirect(login)


def register(request):
    return render(request,'register.html')

def blog(request,id):
    blog = BlogData.objects.get(id=id)
    return render(request,'blog.html',{'blog':blog})


def internships(request):
    cards= BlogData.objects.all().filter(category="Internships").order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards})

def placements(request):
    cards= BlogData.objects.all().filter(category="Placements").order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards})

def general(request):
    cards= BlogData.objects.all().filter(category="General").order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards})

def fests_clubs(request):
    cards= BlogData.objects.all().filter(category="Fests and Clubs").order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards})

def searchMatcher(query,item):
    if query.lower() in item.title.lower() or query.lower() in item.category.lower() or query.lower() in item.desc.lower() or query.lower() in item.student.first_name.lower():
        return True
    else: 
        return False

def search(request):
    search_data = request.GET["search"]
    All = BlogData.objects.all()
    cards = [item for item in All if searchMatcher(search_data,item)]
    if len(cards) == 0:
        return render(request,'explore.html',{'msg':"No Results found..."})
    return render(request,'explore.html',{'cards':cards})
    

def technical(request):
    cards= BlogData.objects.all().filter(category="Technical Blogs").order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards})

def writeblog(request):
    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        if category == 'Category':
            return render(request,'createblog.html',{'msg':"Please select a valid category"})
        blog = request.POST["blog"]
        username = request.user
        blog = BlogData(title = title,desc=blog,student= username,category=category)
        blog.save()
        return redirect('/')
    else:
        return render(request,'createblog.html')

def explore(request):

    cards = BlogData.objects.all().order_by('-date_time')
    
    return render(request,'explore.html',{'cards':cards,'id1':id})

def dashboard(request):
    cards= BlogData.objects.filter(student = request.user)
    return render(request,'myprofile.html',{'cards': cards , 'len':len(cards)})

def update(request,id):
    if request.method == "POST":
        blog = BlogData.objects.get(id=id)
        title = request.POST["title"]
        category = request.POST["category"]
        if category == 'Category':
            return render(request,'createblog.html',{'msg':"Please select a valid category"})
        description = request.POST["blog"]
        username = request.user
        blog.title = title
        blog.category=category
        blog.desc = description
        blog.save()
        cards= BlogData.objects.filter(student = request.user)
        return render(request,'myprofile.html',{'cards': cards , 'len':len(cards)})
    else:
        blog = BlogData.objects.get(id=id)
        return render(request,'updateblog.html',{'blog':blog})
    
def delete(request,id):
    BlogData.objects.filter(id=id).delete()
    cards= BlogData.objects.filter(student = request.user)
    return render(request,'myprofile.html',{'cards': cards , 'len':len(cards)})
