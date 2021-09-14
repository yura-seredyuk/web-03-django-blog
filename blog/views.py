from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog import *
from .models import Post
# Create your views here.

# GET METHOD
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_lists.html', {'posts':posts})
    
