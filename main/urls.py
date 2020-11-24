from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('add', views.addpickup, name='add'),
    path('register', views.registerPage, name='register'),
    path('payment', views.payment, name='payment'),
    path('maps', views.maps, name='maps'),
    path('pickup', views.pickup, name='pickup'),
    path('tracking', views.tracking, name='tracking'),
    path('transactions', views.transactions, name='transactions'),
    path('profile', views.profile, name='profile'),
]
