from django.contrib import admin
from django.urls import path
from landing_page.views import *
from django.contrib.auth.views import LoginView
from auth_user.form import UserLoginForm
from admin_user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing-page"),
    path('login/', LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserLoginForm
    ), name="login"),
     path('dashboard/', dashboard, name="dashboard"),
]
