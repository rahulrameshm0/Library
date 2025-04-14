from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Author, Book, Borrow

# Create your views here.

def home(request):
   return render(request, "home.html")

def user_login(request):
    if request.user.is_authenticated:
        return render(request, "library.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
      
        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            response = render(request, "library.html")  
            response['Cache-control'] = "no-cache, no-store, must-revalidate"
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
        else:
            messages.error(request, "Your password or email is incorrect")
            return redirect('user_login')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
       email = request.POST["email"]
       username = request.POST["username"]
       password = request.POST["password"]

       if User.objects.filter(email=email).exists():
            messages.error(request, "This email address already exist")
            return redirect("signup")
       
       if User.objects.filter(username=username).exists():
           messages.error(request, "This username alreay exist")
           return redirect("signup")
       
       create_user = User.objects.create_user(email=email, username=username, password=password)
       create_user.save()
       messages.success(request, "Signup successful")
       return redirect("user_login")
    
    return render(request, "signup.html")

def add_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Author.objects.create(name=name)
        return redirect('add_author')
    return render(request, "author.html")

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        rating = request.POST.get("rating")
        author_id = request.POST.get("author") 
        if title and rating and author_id:
            Book.objects.create(title=title, rating=rating, author_id=author_id)
        return redirect("add_book")
    authors = Author.objects.all()
    return render(request, 'books.html',{'authors':authors})


def book_details(request):
    book_details = Book.objects.all()
    author = Author.objects.all()

    return render(request, 'book_list.html', {'book_details':book_details, 'author':author})

def user_borrowed(request):
    return render(request, 'user_borrowed.html')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    author = book.author
    if request.method == "POST":
        book.title = request.POST.get('book_name')
        author.name = request.POST.get('author')
        book.save()
        author.save()
        return redirect('book_list')
    return render(request, 'edit.html', {'book':book, 'author':author})

def borrow_book(request, book_id):
    if request.method == "POST":
        print("Borrow view called")
        book = get_object_or_404(Book, id=book_id)
        user_id =request.session.get('user_id')

        if user_id:
            user_obj = get_object_or_404(User, id=user_id)
            Borrow.objects.create(user=user_obj, book=book)
        else:
            messages.error(request, "You need to login first")
            return redirect('user_login')
    return redirect('home')

def delete_item(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("book_list")

def user_logout(request):
    logout(request)
    response = redirect("user_login")
    response['Cache-control'] = "no-cache, no-store, must-revalidate"
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


@login_required
def library(request):
    pass    