from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from messaging.models import Message
from .models import Profile, Post
from .forms import UserRegisterForm, UserProfileForm, PostForm
from messaging.forms import MessageForm

# Vista para index (ver posts)
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/index.html', {'posts': posts})

# Vista para login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

# Vista para logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Vista para registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})

# Vista para editar perfil
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'blog_app/profile_view.html', {'profile_form': profile_form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')  # Redirigir a la lista de posts
    else:
        form = PostForm()
    return render(request, 'blog_app/post_form.html', {'form': form})

# Editar un post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirigir a la lista de posts
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog_app/post_form.html', {'form': form})

# Eliminar un post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirigir a la lista de posts
    
    return render(request, 'blog_app/post_confirm_delete.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_app/post_detail.html', {'post': post})