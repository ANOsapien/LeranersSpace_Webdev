from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# def signup(request):
#     if request.method == 'POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

        
#         if User.objects.filter(username=email).exists():
#             messages.error(request, "An account with this email already exists.")
#             return redirect('signup')

#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')

#         try:
           
#             myuser = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=pass1)
#             myuser.save()
#             messages.success(request, "Your account has been successfully created.")
#             login(request, myuser)
#             return redirect('index')  
#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")
#             return redirect('signup')

#     return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('signup')

        try:
            myuser = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=pass1)
            myuser.save()

            login(request, myuser)

            messages.success(request, "Your account has been successfully created.")
            return redirect('index')  
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')

    return render(request, 'signup.html')
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=email, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('signin')

    return render(request, 'signin.html')

def signout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('index')  \

def index(request):
    return render(request, 'index.html')
