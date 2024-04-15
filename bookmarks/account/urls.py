# custom url for the account
from django.urls import path

#importing views

from . import views

# route
urlpatterns =[
    path('login/',views.user_login,name='login'),
]