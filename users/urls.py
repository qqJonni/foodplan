from django.urls import path
from users.views import login, lk, registration

app_name = 'users'

urlpatterns = [
    path("login/", login, name='login'),
    path('lk/', lk, name='lk'),
    path('registration/', registration, name='registration')
]