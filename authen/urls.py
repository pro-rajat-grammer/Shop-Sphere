

from django.urls import path
from .views import *

urlpatterns=[
    path('login_',login_,name='login_'),
    path('register',register,name='register'),  
    path('logout_',logout_,name='logout_')
]