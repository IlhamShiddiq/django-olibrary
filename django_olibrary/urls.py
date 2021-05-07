from django.contrib import admin
from django.urls import path
from landing_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing-page"),
]
