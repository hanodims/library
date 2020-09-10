from django.shortcuts import render, redirect
from .models import Person,Book,Borrow,User,Search
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

def noo(request):
    context = {
        "msg": 'you have no access!',
    }
    return render(request, 'no.html', context)



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            messages.success(request, "Successfull!")
            return redirect("book-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, "Successfull!")
                return redirect('book-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")


def book_list(request):
    context = {
        "books":Book.objects.all()
    }
    return render(request, 'list.html', context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
    }
    return render(request, 'detail.html', context)


def book_create(request):
    if not (request.user.is_staff):
        return redirect('No')
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfull!")
            return redirect('book-list')
    context = {
        "form":form,
    }
    return render(request, 'bookcreate.html', context)

"""def book_search(request):
    form = SearchForm()
    books = Book.objects.all()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            key = search.searchBy
            keyword = search.keyword
            if (key in ['title','gener','ISPN']):
                search.books = books.filter(title__contains=keyword)
                search.save()
            return redirect('book-list')
    context = {
        'form' : form,
        'results' : books
    }
    return render(request, 'booksearch.html', context)"""
def book_search(request):
    form = SearchForm()
    books = Book.objects.all()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            return redirect('book-list')
    context = {
        'form' : form,
        'results' : books
    }
    return render(request, 'booksearch.html', context)

def admin_profile(request):
    if not request.user.is_staff:
        return redirect("No")
    context = {
        "users": User.objects.all(),
    }
    return render(request, 'profile.html', context)


def user_profile(request):
    if request.user.is_staff or not request.user.is_authenticated:
        return redirect("No")

    userName = request.user.username
    user_obj = Person.objects.get(name=request.user)
    logs = user_obj.borrow_set.all()

    context = {
        "user": User.objects.get(username=userName),
        "logs": logs 
    }
    return render(request, 'profile.html', context)


    
def profile_detail(request, user_id):
    if not request.user.is_staff:
        return redirect("No")
    person = User.objects.get(id=user_id)
    try:
        member = Person.objects.get(name=person)
    except ObjectDoesNotExist:
        return redirect('member-create',person_id=user_id)
    context = {
        "person" : person,
        "member" : member
    }
    return render(request, 'profile-detail.html', context)

    
 

def member_create(request,person_id):
    if not (request.user.is_staff):
        return redirect('No')
    form = MemberForm()
    person = User.objects.get(id=person_id)
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.name = person
            member.save()
            messages.success(request, "Successfull!")
            return redirect('admin-profile')
    context = {
        "form":form,
        "person":person
    }
    return render(request, 'membership.html', context)

    
def book_borrow(request,book_id):
    book_obj = Book.objects.get(id=book_id)
    if book_obj.available == False:
        return redirect('No')
    form = BorrowForm()
    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            book_obj.available = False
            book_obj.save()
            borrow.save()
            messages.success(request, "Successfull!")
            return redirect('book-list')
    context = {
        "form":form,
        "book":book_obj,
    }
    return render(request, 'borrow.html', context)

def book_return(request,book_id):
    book_obj = Book.objects.get(id=book_id)
    book_obj.available = True
    book_obj.save()
    return redirect('book-list')

    context = {
      "book_obj":book_obj 
    }
    return render(request, 'bookreturn', context)

def book_logs(request,book_id):
    book_obj = Book.objects.get(id=book_id)
    logs = book_obj.borrow_set.all()
    
    context = {
      "logs":logs 
    }
    return render(request, 'logs.html', context)
    