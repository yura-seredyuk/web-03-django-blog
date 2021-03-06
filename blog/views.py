from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from blog import *
from .models import Post
from .forms import PostForm, ContactForm, LoginForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

# GET METHOD
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_lists.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# POST METHOD
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


# UPDATE METHOD
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form, 'pk':pk})

# DELETE METHOD
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post:
        post.delete()
        posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
        return render(request, 'blog/post_lists.html', {'posts':posts})

# SEND MAIL

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Title of mail"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'from@mail.com', ['to_help@mail.com'])

            except BadHeaderError:
                return HttpResponse('Find incorrect header!')
            messages.success(request, "Message sent." )
            return redirect('contact')
        messages.error(request, "Error. Message not sent.")
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form':form})

# LOGIN
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            client_data = form.cleaned_data
            user = authenticate(username=client_data['username'], password=client_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successful!')
                else:
                    return HttpResponse('User blocked!')
            else:
                return HttpResponse('User not found!')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})
        
