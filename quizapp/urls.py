from django.urls import path
from quizapp.views import *


urlpatterns = [
    path('', home ,name='home'),
    path('login/', loginPage ,name='login'),
    path('logout/', logoutPage ,name='logout'),
    path('register/', registerPage ,name='register'),
]
