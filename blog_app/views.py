from django.shortcuts import render, HttpResponse,redirect
from blog_app.models import Post, BlogComments
from django.contrib import messages
from django.contrib.auth.models import User 



# Create your views here.

def blog(request):
    allpost = Post.objects.all()
    
    context = {'allPosts': allpost}
    return render(request, "blog/bloghome.html", context)


def blogPost(request, slug):
    blogpost = Post.objects.filter(slug=slug).first()
    comments = BlogComments.objects.filter(post=blogpost)
    context = {'post':blogpost ,'comments':comments,'user':request.user}
    return render(request, "blog/blogpost.html",context)


def addblog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        slug = title
        addb = Post(title=title,author=author,slug = slug,content=content)
        addb.save()
        messages.success(request, "Blog is added successfully!!")
        return redirect('/blog')
    

def blogComments(request):
    if request.method == 'POST':
        postsno = request.POST.get('postsno')
        comment = request.POST.get('comment')
        user = request.user
        # post = Post.POST.get(sno=postsno)
        post = Post.objects.get(sno=postsno)
        comments = BlogComments(comment= comment,user=user,post=post)    
        comments.save()
        messages.success(request, "Successfully  Commented!!")
        

    return redirect(f"/blog/{post.slug}")
    


