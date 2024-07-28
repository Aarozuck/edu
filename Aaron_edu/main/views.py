from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# main/views.py

from django.shortcuts import render
from .models import Tutorial, Book, Tutor, BlogPost, Vacancy

def home(request):
    return render(request, 'home.html')

def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    grades = {}

    for tutorial in tutorials:
        if tutorial.grade_level not in grades:
            grades[tutorial.grade_level] = {}
        if tutorial.subject not in grades[tutorial.grade_level]:
            grades[tutorial.grade_level][tutorial.subject] = []
        grades[tutorial.grade_level][tutorial.subject].append(tutorial)

    return render(request, 'tutorial_list.html', {'grades': grades})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutor_list.html', {'tutors': tutors})

def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})
