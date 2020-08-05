from django.urls import path
from . import views

app_name = 'basicApp'

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('user_login',views.user_login,name='user_login'),
]
