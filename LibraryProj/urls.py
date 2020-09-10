"""LibraryProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('no/',views.noo ,name='No'),

    path('list/', views.book_list, name ="book-list"),
    path('search/', views.book_search, name ="book-search"),
    path('bookcreate/', views.book_create, name ="book-create"),
    path('<int:book_id>/detail/',views.book_detail ,name='book-detail'),
    path('<int:book_id>/borrow/',views.book_borrow ,name='book-borrow'),
    path('<int:book_id>/bookreturn/', views.book_return, name ="book-return"),
        path('<int:book_id>/booklogs/', views.book_logs, name ="book-logs"),

    path('signup/', views.signup, name ="signup"),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

    path('adminprofile/', views.admin_profile, name ="admin-profile"),
    path('profile/', views.user_profile, name ="user-profile"),
    path('<int:user_id>/profiledetail/',views.profile_detail ,name='profile-detail'),
    path('<int:person_id>/membership/',views.member_create ,name='member-create'),
]
