from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import datetime

# add models
from homepost.models import Posts
from login.models import Member 


# add Forms
from homepost.forms import FormAddPost,FormDeletPost,FormUpdatePost




# Create your views here.

def home_post(request):
    try:
        mymember = Member.objects.get(status = "active")
        name = mymember.username
        email = mymember.email
        gender = mymember.gender
        
        
        mypost = Posts.objects.all()
        
        
        return render(request,'hposts/homepost.html',{"items" : mypost, 'name': name , 'email': email, 'gender' : gender})
    
    except:
        
        return render(request,'sign/login.html')






# get
def add_post(request):
    try:
        mymember = Member.objects.get(status = "active")
        name = mymember.username
        email = mymember.email
        gender = mymember.gender

        
        
        return render(request,'hposts/addpost.html', {'name' : name,'email' : email,'gender' : gender})
    except:
        return render(request,'sign/login.html')

    
# post
def add_post_succes(request):
    
    
    topic = ''
    content = ''
    email = ''
    picture = ''
    
    if request.method == 'POST':
        
        MyAddForm = FormAddPost(request.POST)

        if MyAddForm.is_valid():
            
                       
            postAdd = Posts(
                topic = MyAddForm.cleaned_data['topic'],
                content = MyAddForm.cleaned_data['content'],
                # datatime = datetime.datetime().now().date,
                user = MyAddForm.cleaned_data['email'],
                # picture = MyAddForm.cleaned_data['picture']
                
            )
            postAdd.save()
            
            mypost = Posts.objects.all()
            
            mymember = Member.objects.get(status = "active")
            email = mymember.email
        
            return render (request,"hposts/homepost.html",{"items" : mypost, 'email' : email})
        
        return HttpResponse("if faild")
        
    return HttpResponse("post faild")
    
    


def delete_post(request):

    try:
        id = ''
        if request.method == 'POST':
            myidform = FormDeletPost(request.POST)
            if myidform.is_valid():
                id = myidform.cleaned_data['id']
                
                mypost = Posts.objects.get(id = id)
                
                mypost.delete()
                
                return render(request, 'hposts/homepost.html')

        return HttpResponse("error")
    except:
        return render(request,'sign/login.html')



# get
def update_post(request):
    try:
        mymember = Member.objects.get(status = "active")
        name = mymember.username
        gender = mymember.gender
        
        
        id = ""
        myposts = ""
        if request.method == 'POST':
            myidform = FormDeletPost(request.POST)
            if myidform.is_valid():
                id = myidform.cleaned_data['id']
                try:
                    myposts = Posts.objects.get(id = id)
                except:
                    myposts = None
                    
            return render(request,'hposts/updatepost.html', {'myposts' : myposts, 'name': name, 'gender' : gender})
        
        
        
        return HttpResponse("error")
    except:
        return render(request,'sign/login.html')

# post
def update_post_updated(request):
    try:
        id = ""
        topic = ''
        content = ''
        email = ''
        if request.method == 'POST':
            myformupdate = FormUpdatePost(request.POST)
            if myformupdate.is_valid():
                id = myformupdate.cleaned_data['id']
                topic = myformupdate.cleaned_data['topic']
                content = myformupdate.cleaned_data['content']
                email = myformupdate.cleaned_data['email']
                
                
                mypost = Posts(
                    id = id,
                    topic = topic,
                    content = content,
                    user = email
                )
                
                mypost.save()
                
                
                return render(request,"hposts/homepost.html")
        
        return HttpResponse("error")
    except:
        return render(request,'sign/login.html')


def select_post(request):
    
    try:
        mymember = Member.objects.get(status = "active")
        email = mymember.email
        name = mymember.username
        gender = mymember.gender
        
        myposts = Posts.objects.all().filter(user = email)
        
        return render(request,'hposts/selectpost.html',{'myposts' : myposts, 'name' : name,'gender' : gender})
    except:
        return render(request,'sign/login.html')



def logout(request):

    try:
        Member.objects.filter(status = 'active').update(status = "off")

        
        return render(request, 'sign/login.html')
    except:
        return render(request,'sign/login.html')
        