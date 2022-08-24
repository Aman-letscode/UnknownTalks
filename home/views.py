from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog_app.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 


# Create your views here.

def home(request):
    return render(request, "home/home.html")
    # return HttpResponse("This is the home page")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<10:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, "Successfully Sent!!")
        print(name,email,phone,content)
        
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']

    # Checking if it is more than the required length
    if len(query)>78:
        allPost = Post.objects.none() #Clearing the object and displaying error
    else:
        allPosttitle = Post.objects.filter(title__icontains=query)
        allPostAuthor = Post.objects.filter(author__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPost = allPosttitle.union(allPostAuthor,allPostContent)
    if allPost.count() == 0: #checking if there are no post
        messages.warning(request,"No search results found. Please refine your query")
    params = {'allPost':allPost,'query':query} #making a dictionary
    # print(allPost)
    return render(request, "home/search.html",params)


    # allPost = Post.objects.filter(title__icontains=query)
    # context = {'posts':allPost}
    # return render(request, "home/search.html",context)




def handleSignUp(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #validate the user
        if len(username)<5:
            messages.error(request, "Your username must contain more than 5 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers!!")
            return redirect('home')
        
        if pass1!=pass2:
             messages.error(request, "Passwords do not match")
             return redirect('home')



        #Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Id has been created Successfully!!")
        return redirect('home')
    else:
        HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']


        user = authenticate(username=loginusername,password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password")
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')