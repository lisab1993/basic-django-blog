from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'chirpapp/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        print(request.user, 'request.user')
        title = request.POST.get('title')
        text = request.POST.get('text')
        Post.objects.create(
            title=title,
            text=text,
            author=request.user,
            created_date=timezone.now()
        )
        return redirect('chirpapp:index')

#This view has two jobs: to grab the information from the post being edited, and to submit the changes.
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.save()
        return redirect('chirpapp:index')
    return render(request, 'chirpapp/edit.html', context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('chirpapp:index')
