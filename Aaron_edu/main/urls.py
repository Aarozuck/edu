from django.urls import path
from .views import blog_list, book_list, register, login_view, tutor_list, tutorial_list,home, vacancy_list

urlpatterns = [
      path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('tutorials/', tutorial_list, name='tutorial_list'),
    path('books/', book_list, name='book_list'),
    path('tutors/', tutor_list, name='tutor_list'),
    path('blogs/', blog_list, name='blog_list'),
    path('vacancies/', vacancy_list, name='vacancy_list'),
]
