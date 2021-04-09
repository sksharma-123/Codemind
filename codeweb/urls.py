from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<slug:user>/', views.profile, name="profile"),
    path('login-request/', views.login_request, name="login_request"),


    path('python-ide/', views.python_ide, name="python_ide"),
    path('java-ide/', views.java_ide, name="java_ide"),
    path('c-ide/', views.c_ide, name="c_ide"),


    path('python-sub/', views.python_sub, name="python_sub"),
    path('java-sub/', views.java_sub, name="java_sub"),
    path('c-sub/', views.c_sub, name="c_sub"),


    path('code-submitted/', views.code_submitted, name="code_submitted"),
    path('python-collec/', views.python_collec, name="python_collec"),
    path('java-collec/', views.java_collec, name="java_collec"),
    path('c-collec/', views.c_collec, name="c_collec"),


    path('python-collec/<uuid:uid>/', views.show_python_code, name="show_python_code"),
    path('java-collec/<uuid:uid>/', views.show_java_code, name="show_java_code"),
    path('c-collec/<uuid:uid>/', views.show_c_code, name="show_c_code"),
]
