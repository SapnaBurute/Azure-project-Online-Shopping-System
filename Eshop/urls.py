"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Eshop.views import home,login,signup,cart,orders,userProfile,forget_password
from item_card.middleware.auth import auth_middleware

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.HomePage.as_view(), name= 'homePage' ),
    path('signUp/',signup.SignUp.as_view(), name='signUp_page' ),
    path('login/',login.Login.as_view(), name='login_page' ),
    path('cart/',cart.Cart.as_view(), name='cart_page' ),
    path('logOut/',login.logOut, ),
    path('check-out/',auth_middleware(cart.Check_out.as_view()),name='check_out' ),
    path('orders-page/',auth_middleware(orders.Your_Order.as_view()),name='orders_page' ),
    path('user-profile/',auth_middleware(userProfile.UserProfile.as_view()),name='user_profile'),
    path('change-password/',auth_middleware(userProfile.Change_password.as_view()),name='change_password'),
    path('forget_password/',(forget_password.ForgetPassword.as_view()),name='forget_password'),
    path('OTP_Verify/',(forget_password.OTPVerify.as_view()),name='OTP_Verify'),
    path('new_password/',(forget_password.NewPassword.as_view()),name='new_password'),

 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
