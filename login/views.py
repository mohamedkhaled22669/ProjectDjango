from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# forms
from login.forms import RegisterForm , LoginForm

# models
from login.models import Member
from homepost.models import Posts


# Create your views here.



# get
def register(request):
    
    return render(request, 'sign/register.html')

# post
def register_accept(request):
    
    username = "u"
    email = "e"
    password = "p"
    gender = "m"
    
    if request.method == "POST":
        myregisterform = RegisterForm(request.POST)
        if myregisterform.is_valid():
            username = myregisterform.cleaned_data['username']
            email = myregisterform.cleaned_data['email']
            password = myregisterform.cleaned_data['password']
            gender = myregisterform.cleaned_data['gender']

            # myobject = Member.objects.get(email = email)

            try:
                myobject = Member.objects.get(email=email)
            except Member.DoesNotExist:
                myobject = None
            
            if (myobject):
                
                return render (request, 'sign/register.html',{'email_is_exist': "email_is_exist"})

            else:
                
                mymember = Member(
                    username = username,
                    email = email,
                    password = password,
                    gender = gender,
                    status = "off",
                )
                
                mymember.save()
                
                return render(request,'sign/login.html',{'login_success' : "login_success"})

    else:
        # ??
        myregisterform = RegisterForm()
    # ??
    return render(request, 'sign/myerror.html',{"username" : username, "form" : myregisterform})   
#   return HttpResponse('error last if')
    
    
# # get
# def login(request):
    
#     return render(request, 'sign/login.html')



# post
def login_accept(request):

    email = ""
    password = ''
    
    if request.method == 'POST':
        myLoginForm = LoginForm(request.POST)
        if myLoginForm.is_valid():
            email = myLoginForm.cleaned_data['email']
            password = myLoginForm.cleaned_data['password']

            try:
                
                user = Member.objects.get(email = email)
                
            except:
                
                user = None
            
            if (user and password == user.password):
                
                Member.objects.filter(email = user.email).update(status = "active") 
                
                try:
                    mymember = Member.objects.get(status = "active")
                    name = mymember.username
                    email = mymember.email
                    gender = mymember.gender
                    
                    
                    mypost = Posts.objects.all()
                    
                    
                    return render(request,'hposts/homepost.html',{"items" : mypost, 'name': name , 'email': email, 'gender' : gender})
                
                except:
                    
                    return render(request,'sign/login.html')
                
                return render(request, 'hposts/homepost.html',{})

            else:
                
                return render (request, 'sign/login.html',{'fail' : "fail"})

    else:
        myLoginForm = LoginForm()
        
    return HttpResponse('error last if')