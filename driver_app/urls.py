from django.urls import path
from . import views

urlpatterns = [
    path('driver_login', views.driver_login_page, name='driver_login'),
    path('driver/logout', views.driver_logout, name='logout'),
    path('driver_register', views.register_driver_page, name='driver_register'),
    path('driver_profile', views.driver_profile, name='driver_profile'),
    path('driver_pickup', views.driver_pickup, name='driver_pickup'),
    path('driver_transaction_log', views.driver_transaction_log, name='driver_transaction_log'),
    path('driver_home', views.driver_home_page, name='driver_home'),
    path('driver_profile_edit', views.driver_profile_edit, name='driver_profile_edit'),

]