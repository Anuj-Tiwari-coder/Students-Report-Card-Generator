from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Student, SubjectMarks
from django.db.models import Sum
from .seed import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'Report/home.html')

@login_required(login_url="/login")
def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search= request.GET.get('search')
        queryset= queryset.filter(
            Q(student_name__icontains= search ) |
            Q(department_department__icontains= search) |
            Q(student_id__student_id__icontains= search) |
            Q(student_age__icontains= search) |
            Q(student_email__icontains= search )|
            Q(student_contact__icontains= search )
            )

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number )

    print(page_obj.object_list)
    return render(request, 'Report/students.html',{'queryset': page_obj})

@login_required(login_url="/login")
def see_marks(request, student_id):
    queryset= SubjectMarks.objects.filter(student__student_id__student_id= student_id)
    Total_marks=queryset.aggregate(Total_marks=Sum('marks'))
    return render(request, 'Report/see_marks.html', {'queryset': queryset,'Total_marks': Total_marks})

def login_page(request):
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "User Already exist.")
            return redirect('/login/')
        
        user= authenticate(username = username, password = password )
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/students/')
        

    return render(request, 'Report/login.html')

@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return redirect ('/login/')

def register_page(request):
    if request.method == "POST":
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        username= request.POST.get("username")
        password= request.POST.get("password")

        user= User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Oops Username Already Taken please! Select New One.")
            return redirect('/register/')
        
        user=User.objects.create(
                                first_name = first_name,
                                last_name = last_name,
                                username = username)
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")
        return redirect('/register/')
    return render(request, 'Report/register.html')
