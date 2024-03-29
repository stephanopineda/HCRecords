from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_client, name="logout"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),

    path('staffdashboard/', views.staff_dashboard, name="staff_dashboard"),
    path('userdashboard/', views.user_dashboard, name="user_dashboard"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('unverifiedforms/', views.unverifiedforms, name="unverifiedforms"),
    path('viewrecords/', views.view_records, name="view_records"),
    path('manage-users/', views.manage_users, name="manage_users"),
    path('learn-more/', views.learn_more, name="learn_more"),
]
