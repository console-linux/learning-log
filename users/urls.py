#URL schemes 4 users

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #reg_page
    path('register/', views.register, name='register')
]