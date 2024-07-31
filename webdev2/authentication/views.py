from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserDetailsForm, UsernamePasswordForm, LoginForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Post

def signup_stage1(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            request.session['fname'] = form.cleaned_data['fname']
            request.session['lname'] = form.cleaned_data['lname']
            request.session['email'] = form.cleaned_data['email']
            return redirect('signup_stage2')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserDetailsForm()
    return render(request, 'signup_stage1.html', {'form': form})

def signup_stage2(request):
    if 'fname' not in request.session or 'lname' not in request.session or 'email' not in request.session:
        return redirect('signup_stage1')

    if request.method == 'POST':
        form = UsernamePasswordForm(request.POST)
        if form.is_valid():
            fname = request.session['fname']
            lname = request.session['lname']
            email = request.session['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['pass1']

            try:
                myuser = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
                myuser.save()
                login(request, myuser)
                messages.success(request, "Your account has been successfully created.")
                return redirect('index')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return redirect('signup_stage2')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UsernamePasswordForm()
    return render(request, 'signup_stage2.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('my_posts')
        else:
            messages.error(request, "Error creating post. Please correct the errors below.")
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('my_posts')
        else:
            messages.error(request, "Error updating post. Please correct the errors below.")
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('my_posts')
    return render(request, 'confirm_delete_post.html', {'post': post})
