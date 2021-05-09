from django.contrib import admin
from django.urls import path
from landing_page.views import *
from django.contrib.auth.views import LoginView, LogoutView
from auth_user.form import UserLoginForm
from admin_user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing-page"),
    path('login/', LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserLoginForm
    ), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard, name="dashboard"),
    path('book/', book, name="book"),
    path('member/', member, name="member"),
    path('publisher/', publisher, name="publisher"),
    path('publisher/add/', add_publisher, name="add_publisher"),
    path('publisher/edit/', edit_publisher, name="edit_publisher"),
    path('category/', category, name="category"),
    path('transaction/', transaction, name="transaction"),
    path('report/', report, name="report"),
]
