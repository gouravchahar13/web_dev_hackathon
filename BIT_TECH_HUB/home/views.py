from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.



# home page functions
@login_required(login_url="/login/")
def home(request):
    if request.method=="POST":
        data=request.POST
        rec_name=data.get('Recipe_name')
        rec_des=data.get('Recipe_Desciption')
        Form_image = request.FILES['Recipe_Img']

        Recipe.objects.create(
            Recipe_name=rec_name,
            Recipe_Desciption=rec_des,
            Recipe_Img=Form_image,
        )
        return redirect('/')
    
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        queryset= queryset.filter(Recipe_name__icontains=request.GET.get('search'))
    ls=[0,1,2,3]
    context={'recipe':queryset,'i':ls}


    return render(request,'index.html',context)

@login_required(login_url="/login/")
def delete_rec(request,id):
    delete_obj=Recipe.objects.get(id=id)
    delete_obj.delete()
    return redirect('/')

@login_required(login_url="/login/")
def update_rec(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        rec_name=data.get('Recipe_name')
        rec_des=data.get('Recipe_Desciption')
        rec_img = request.FILES['Recipe_Img']
        queryset.Recipe_name=rec_name
        queryset.Recipe_Desciption=rec_des
        queryset.Recipe_Img=rec_img
        queryset.save()
        return redirect("/")
    return render(request,'update.html',context={'Recipe':queryset})



# accounts functions 


# register functions 

def register(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        f_n=data.get('first_name')
        l_n=data.get('last_name')
        email=data.get('email')
        user=User.objects.create(
            first_name=f_n,
            last_name=l_n,
            username=username,
            email=email,
        )
        u_n=User.objects.filter(username=username)
        user.set_password(password)
        user.save()
        if not u_n.exists():
            messages.info(request, "username exists enter a different one")
            return redirect("/register/")
        messages.info(request, "account created successfully")
        send_mail(
        "BIT_TECH_HUB",
        f"Hello {f_n},\n You Have successfully registered on BIT_TECH_HUB please maintain the decorum of this platform",
        "tutorialjaat13@gmail.com",
        [email,],
        fail_silently=False,
        )
        return redirect('/login/')
    return render(request,'register.html')


# login functions 

def login_pg(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "invalid username")
            return redirect("/login/")
        else:
            messages.info(request, "success")
        
        user_ok=authenticate(username=username,password=password) 

        if user_ok is None:
            messages.info(request, "Invalid credentials")
            return redirect("/login/")
        else:
            login(request,user_ok)
            return redirect('/login/')

    return render(request,'login.html')



def logout_pg(request):
    logout(request)
    return redirect("/login/")


def delete_user(request,id):
    user = User.objects.filter(username=id)
    email=user[0].email
    user.delete()
    send_mail(
    f"Account Deletion!!!!!",
    "Greetings  ,  You Have successfully deleted your account with username  on BIT_TECH_HUB",
    "tutorialjaat13@gmail.com",
    [email,],
    fail_silently=False,
    )
    messages.info(request, f"The user {id} has been deleted successfully")
    return redirect("/")


