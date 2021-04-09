from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('add', views.add_pickup, name='add'),
    path('register', views.register_page, name='register'),
    path('payment', views.payment, name='payment'),
    path('maps', views.maps, name='maps'),
    path('pickup', views.pickup, name='pickup'),
    path('tracking', views.tracking, name='tracking'),
    path('transactions', views.transactions, name='transactions'),
    path('profile', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('drivers', views.drivers, name='drivers'),

]
