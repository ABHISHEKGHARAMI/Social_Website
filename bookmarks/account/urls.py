# custom url for the account
from django.urls import path
# importing the auth views   
from django.contrib.auth import views as auth_views

#importing views

from . import views

# route
urlpatterns =[
   # path('login/',views.user_login,name='login'),
   path('login/',auth_views.LoginView.as_view(),name="login"),
   path('logout/',auth_views.LogoutView.as_view(),name="logout"),
   path('',views.dashboard,name="dashboard"),
]