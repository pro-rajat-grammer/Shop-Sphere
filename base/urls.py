
from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('contactus',contactus,name='contactus'),
    path('addcart/<int:id>',addcart,name='addcart'),
    path('profile',profile,name='profile'),
    path('cart',cart,name='cart'),
    path('cartitemrem/<int:id>',cartitemrem,name='cartitemrem'),
    path('checkoutform',checkoutform,name='checkoutform'),
    path('placeorder',placeorder,name='placeorder'),
    
]