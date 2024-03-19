from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_client, name="logout"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),

    path('profile/', views.user_profile, name="profile"),

    path('dashboard/', views.staff_dashboard, name="staff_dashboard"),
    path('', views.home, name="home"),
]
