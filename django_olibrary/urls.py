from django.contrib import admin
from django.urls import path, include
from landing_page.views import *
from django.contrib.auth.views import LoginView, LogoutView
from auth_user.form import UserLoginForm
from admin_user.views import *
from transaction.views import *
from django.conf.urls.static import static

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
    path('book/add/', add_book, name="add_book"),
    path('book/edit/<int:book_id>', edit_book, name="edit_book"),
    path('book/detail/<int:book_id>', detail_book, name="detail_book"),
    path('book/delete/', delete_book, name="delete_book"),
    path('member/', member, name="member"),
    path('member/add/', add_member, name="add_member"),
    path('member/edit/<int:member_id>', edit_member, name="edit_member"),
    path('member/detail/<int:member_id>', detail_member, name="detail_member"),
    path('member/delete/', delete_member, name="delete_member"),
    path('publisher/', publisher, name="publisher"),
    path('publisher/add/', add_publisher, name="add_publisher"),
    path('publisher/edit/<int:publisher_id>', edit_publisher, name="edit_publisher"),
    path('publisher/delete/', delete_publisher, name="delete_publisher"),
    path('category/', category, name="category"),
    path('category/add/', add_category, name="add_category"),
    path('category/edit/<int:category_id>', edit_category, name="edit_category"),
    path('category/delete/', delete_category, name="delete_category"),
    path('transaction/', transaction, name="transaction"),
    path('transaction/validation/', member_validation, name="validation"),
    path('transaction/submit/', submit_transaction, name="submit_transaction"),
    path('transaction/cancel/', cancel_transaction, name="cancel_transaction"),
    path('transaction/add/', add_transaction, name="add_transaction"),
    path('transaction/return/<int:transaction_id>', returning, name="returning"),
    path('report/', report, name="report"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)