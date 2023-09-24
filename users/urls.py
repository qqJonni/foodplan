from django.urls import path
from users.views import login, lk, registration, logout, create_order

app_name = 'users'

urlpatterns = [
    path("login/", login, name='login'),
    path('lk/', lk, name='lk'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('create_order/', create_order, name='create_order')
]