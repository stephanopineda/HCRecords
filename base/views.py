from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegistrationForm
from functools import wraps

# Home
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# Authentication Functions
def register_page(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        context = {'form': form}

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('user_dashboard')
            else: 
                # Add form errors to context
                context['form'] = form
                # Display form errors as messages
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, 'base/register.html', context)
    else:
        return redirect('home')


def login_page(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username').lower()
            password = request.POST.get('password')
            
            # Check if Username exists
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username')
                return redirect('login')
            
            # Authenticate 
            user = authenticate(request, username=username, password=password)
            
            # If user was returned, login. Otherwise, invalid password
            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return redirect('staff_dashboard')
                else:
                    return redirect('user_dashboard')
            else: 
                messages.error(request, "Invalid Password")
                return redirect('login')
            
        return render(request, 'base/login.html', context)
    else:
        # redirect to home if already authenticated
        return redirect('home')

def logout_client(request):
    logout(request)
    return redirect('home')


# User and Staff Views
@login_required(login_url='home')
def user_dashboard(request):
    user = User.objects.get(id=request.user.id)   
    context = {user: 'user'}
    return render(request, 'base/user_dashboard.html', context)


# Staff Dashboard and Side Bars

def staff_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')  
        elif not request.user.is_staff:
            return redirect('home')  
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

@staff_login_required
def staff_dashboard(request):
    total_users = User.objects.count()
    context = {'total_users': total_users}
    return render(request, 'base/staff_dashboard.html', context)

@staff_login_required
def dashboard(request):
    total_users = User.objects.count()
    context = {'total_users': total_users}
    return render(request, 'base/staff-section/dashboard.html', context)

@staff_login_required
def unverifiedforms(request):
    context = {}
    return render(request, 'base/staff-section/unverifiedforms.html', context)

@staff_login_required
def view_records(request):
    context = {}
    return render(request, 'base/staff-section/view_records.html', context)

@staff_login_required
def manage_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'base/staff-section/manage_users.html', context)

@staff_login_required
def learn_more(request):
    context = {}
    return render(request, 'base/staff-section/learn_more.html', context)



# User CRUD
def patient_view_form(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_create_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_update_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_unsubmit_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')


# Staff CRUD
def patient_view_form(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_create_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_update_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')

def patient_unsubmit_form_(request):
    context = {}
    #return render(request, 'base/home.html', context)
    return HttpResponse('Patient Dashboard')